import pandas as pd
import datetime
import pytz
import time
import threading
from twarc import Twarc
import os
import tweepy
import constants as cnst
import glob
import os.path as path
from operator import itemgetter
import argparse
from distutils import util
utc=pytz.UTC


# global twarc object
t = Twarc(cnst.consumer_key, cnst.consumer_secret,
		cnst.access_token, cnst.access_token_secret)

def get_latest_df(name):
	"""
	given the file name, this method identifies the most recently "created"
	file and returns path to that file.
	if no file is found with that name or the "creation" time is not accessible
	it returns None.
	"""
	files = glob.glob("{}/{}*.csv".format(cnst.dataset_root_path, name))
	if len(files) == 0:
		return None
	try:
		files_time = [(path.getctime(file), file) for file in files]
	except OSError as err:
		return None
	files_time.sort(key=itemgetter(0), reverse=True)
	return pd.read_csv(files_time[0][1])

def export_dataset(df,name):
	"""
	given a dataframe and a file name, this will write out the dataframe to the file
	"""
	name = "{}/{}_{}.csv".format(cnst.dataset_root_path, name,datetime.datetime.now().strftime("%B_%d_%y_%H"))
	df.to_csv(name, index=False)

def create_original_df():
	"""
	This creates the original dataframe that is used to store the tweets
	"""
	columns = ["tweet_id","created_at","next_update","count"]
	df = pd.DataFrame(columns=columns, )
	return df

def create_df():
	"""
	This creates the original dataframe that is used to store the retweet counts
	"""
	column_names = ['tweet_id','count','created_time','next_update']
	for i in range(1, 101):
		column_names.append(str(i))
	df = pd.DataFrame(columns = column_names)
	return df

def bird_watcher():
	"""
	This thread monitors specified twitter accounts and saves the tweets to a dataframe 
	"""
	global original_df 
	
	if os.path.exists("bird_watcher.log"):
		bird_log = open("bird_watcher.log", "a")
		time_now = datetime.datetime.utcnow().replace(tzinfo=utc)
		log = str("\n["+str(time_now) + "] BIRDWATCHER \t Recovering from Failure")
		bird_log.write(log)
		bird_log.flush()
	else:
		bird_log = open("bird_watcher.log", "a")
	
	# Convert twitter handles from accounts.txt to user IDs
	follow_list = get_userIds()
	follow_str = ",".join([str(x) for x in follow_list])
	
	for tweet in t.filter(follow=follow_str):
		if 'retweeted_status' not in tweet:
			try:
				if tweet['user']['id'] in follow_list \
				and len(tweet['entities']['urls']) != 0 \
				and (original_df['tweet_id'] != tweet['id']).all():
					current = datetime.datetime.now(datetime.timezone.utc)
					datetimePublished = datetime.datetime.strptime(tweet["created_at"], '%a %b %d %H:%M:%S %z %Y')
					nextUpdate =  datetimePublished + datetime.timedelta(hours=24)
					log = str("\n[" + str(current) + "] BIRDWATCHER \t Adding tweet From source "+str( tweet['id'])+"\tcreated_time: "+str(datetimePublished)+"\tnext_update: "+str(nextUpdate))
					#print(log)
					bird_log.write(log)
					bird_log.flush()
					original_df = original_df.append({
							'tweet_id':tweet['id'],
							'created_at' : tweet['created_at'],
							'next_update': nextUpdate,
							'count' : 0 }, ignore_index=True)
			except:
				current = datetime.datetime.now(datetime.timezone.utc)
				log = str("\n[" + str(current) + "] BIRDWATCHER \t Error in conditional")
				#print(log)
				bird_log.write(log)
				bird_log.flush()
		else:
			try:
				if tweet['retweeted_status']['user']['id'] in follow_list \
					and 'extended_tweet' in tweet['retweeted_status'] \
					and 'entities' in tweet["retweeted_status"]["extended_tweet"] \
					and len(tweet["retweeted_status"]["extended_tweet"]["entities"]['urls']) != 0\
					and (original_df['tweet_id'] != tweet['retweeted_status']['id']).all():
					created_time = datetime.datetime.strptime(tweet["retweeted_status"]["created_at"],"%a %b %d %H:%M:%S %z %Y")
					current = datetime.datetime.now(datetime.timezone.utc)
					diff =  current - created_time
					if diff.days == 0:
						current = datetime.datetime.now(datetime.timezone.utc)
						datetimePublished = datetime.datetime.strptime(tweet["retweeted_status"]["created_at"], '%a %b %d %H:%M:%S %z %Y')
						nextUpdate =  datetimePublished + datetime.timedelta(hours=24)
						log = str("\n[" + str(current) + "] BIRDWATCHER \t From retweet "+str(tweet['id'])+" Adding tweet: "+str(tweet["retweeted_status"]["created_at"])+ "\tcreated_time: "+str(datetimePublished)+"\tnext_update: "+str( nextUpdate))
						#print(log)
						bird_log.write(log)
						bird_log.flush()
						original_df = original_df.append({
							'tweet_id':tweet["retweeted_status"]["id"],
							'created_at' : tweet["retweeted_status"]["created_at"],
							'next_update': nextUpdate,
							'count' : 0 }, ignore_index=True)
			except:
				current = datetime.datetime.now(datetime.timezone.utc)
				log = str("\n[" + str(current) + "] BIRDWATCHER \t Error in conditional")
				#print(log)
				bird_log.write(log)
				bird_log.flush()
				
# This thread is responsible for getting the retweets every 24 hrs
def scheduler(df, recover):
	global original_df
	#print("original_df columns :", original_df.columns)
	#print("df columns :", df.columns)
	if os.path.exists("scheduler.log"):
		scheduler_log = open("scheduler.log", "a")
		time_now = datetime.datetime.utcnow().replace(tzinfo=utc)
		log = str("\n["+str(time_now) + "] SCHEDULER \t Recovering from Failure")
		scheduler_log.write(log)
		scheduler_log.flush()
	else:
		scheduler_log = open("scheduler.log", "a")
		
	column_names = ['tweet_id','count','created_time','next_update']
	for i in range(1, 101):
		column_names.append(str(i))
	
	export_counter = 0
	while(1):
		
		# Sleep 5 min
		time.sleep(300)

		#Window size depends on conditions
		if recover is True:
			time_now = datetime.datetime.utcnow().replace(tzinfo=utc)
			time_range = time_now + datetime.timedelta(minutes=15)
			time_travel = time_now - datetime.timedelta(minutes=60)
			recover = False	
		else:
			if export_counter % 2 == 0:
				time_now = datetime.datetime.utcnow().replace(tzinfo=utc)
				time_range = time_now + datetime.timedelta(minutes=15)
				time_travel = time_now - datetime.timedelta(minutes=45)
			else:
				time_now = datetime.datetime.utcnow().replace(tzinfo=utc)
				time_range = time_now + datetime.timedelta(minutes=15)
				time_travel = time_now - datetime.timedelta(minutes=15)
		export_counter +=1
		
		log = str("\n["+str(time_now) + "] SCHEDULER \t Loop starting \ttime_range: "+str(time_travel)+" -> "+str(time_range))
		#print(log)
		scheduler_log.write(log)
		scheduler_log.flush()
		#print("Original DF length from scheduler ",len(original_df))
		
		# A list of (tweet_id)
		retweetables = list()
		retweetables_id = list()
		
		for row in original_df.itertuples():
			try:
				current_update = pd.to_datetime((df.loc[(df.tweet_id == row.tweet_id), 'next_update'])).item()#[0])
			except:
				current_update = pd.to_datetime(row.next_update)
				
			if current_update >= time_travel and current_update <= time_range :
				retweetables_id.append(row.tweet_id)
				retweetables.append(row)
		
		curr_retweets = get_retweets(retweetables_id,t)
		for row  in retweetables:
			# row = original_df.where[original_df['tweet_id']==retweetable_id,["tweet_id","created_at","next_update"]  ]
			# print(row)
			# print(row.tweet_id,row.created_at)
			if row.tweet_id in curr_retweets:
				if(not(row.tweet_id in df.tweet_id.values)):
					next_update = pd.to_datetime(row.next_update) + datetime.timedelta(hours=24)
					current_time = datetime.datetime.utcnow().replace(tzinfo=utc)
					log=str("\n[" + str(current_time)+"] SCHEDULER\t "+str(row.tweet_id)+" first time being added\t create_time: "+str(row.created_at)+"\tcurrent update: " + str(row.next_update)+"\tnext_update: "+str(next_update))
					#print(log)
					scheduler_log.write(log)
					scheduler_log.flush()
					data = { 'tweet_id':[row.tweet_id],
								'count' : 2,
								'created_time': [row.created_at],
								'next_update' : [next_update],
								'1':[curr_retweets[row.tweet_id]]}
					df_temp = pd.DataFrame(data, columns=column_names)
					df_temp = df_temp.fillna(-1)
					df = df.append(df_temp)
				else:
					# print("\n")
					# print("Printing error part",type(df.loc[(df.tweet_id == row.tweet_id), 'next_update']),df.loc[(df.tweet_id == row.tweet_id), 'next_update'])
					# print(df.index)
					# print("\n")
					current_update = ((df.loc[(df.tweet_id == row.tweet_id), 'next_update'])).item()#[0])
					# if(current_update >= time_now and current_update <= time_range):
					current_count = (df.loc[(df.tweet_id == row.tweet_id), 'count']).item()# [0]
					df.loc[(df.tweet_id == row.tweet_id), str(current_count)] = curr_retweets[row.tweet_id]
					new_time = current_update + datetime.timedelta(hours=24)
					current_time = datetime.datetime.utcnow().replace(tzinfo=utc)
					log=str("\n[" + str(current_time)+"] SCHEDULER\t "+str(row.tweet_id)+" update retweets for offset: " +str(current_count)+ "\t create_time: "+str(row.created_at)+"\tcurrent update: " + str(current_update)+"\tnext_update: "+str(new_time))
					#print(log)
					#scheduler_log.write(log)
					scheduler_log.flush()
					df.loc[(df.tweet_id == row.tweet_id), 'next_update'] = new_time
					df.loc[(df.tweet_id == row.tweet_id), 'count'] = (int(current_count) + 1)
				
		#print("\n SCHEDULER \t start_time: ", start_time, "\telapsed: ", elapsed_time)
		if export_counter % 2 == 0:
			log=str("\n["+str(datetime.datetime.utcnow().replace(tzinfo=utc))+"] SCHEDULER\t Writing to file")
			#print(log)
			scheduler_log.write(log)
			scheduler_log.flush()
			log=str("\n["+str(datetime.datetime.utcnow().replace(tzinfo=utc))+"] SCHEDULER\t Original Frame len : "+str(len(original_df))+ " Data Frame len : "+str(len(df)))
			#print(log)
			scheduler_log.write(log)
			scheduler_log.flush()
			if len(df) != 0:
				export_dataset(df, "retweet")
			if len(original_df) != 0:
				export_dataset(original_df, "original_df")
			# df.to_csv('data.csv', index=True)

		log=str("\n["+str(datetime.datetime.utcnow().replace(tzinfo=utc))+"] SCHEDULER\t Loop ending")
		#print(log)
		scheduler_log.write(log)
		scheduler_log.flush()

def get_retweets(tweets, twarc_api, step=100):
	"""
	For all the tweets passed to this method, if retrieves retweets by 
	requesting for 100 retweets at a time.
	:returns: A dictionary with tweet_id as key and retweet_count as value {int:long}
	"""
	retweets = dict()
	for i in range(0,len(tweets),step):
		last_idx = min(i+step, len(tweets))
		sub_list = tweets[i:last_idx]
		for tweet in twarc_api.hydrate(sub_list):
			retweets[tweet['id']]=tweet['retweet_count']
	return retweets


# convert handles to user_ids
def get_userIds():

	# create Tweepy object
	auth = tweepy.OAuthHandler(cnst.consumer_key, cnst.consumer_secret)
	auth.set_access_token(cnst.access_token, cnst.access_token_secret)
	api = tweepy.API(auth)

	# read twitter handles from accounts.txt
	account_list = list()
	account_file = open("accounts.txt", "r")
	accounts = account_file.readlines()
	for account in accounts:
		account_list.append(account.strip())
	account_file.close()

	# convert handles to user ID's
	user_objects = api.lookup_users(screen_names=account_list)
	user_ids = [user.id_str for user in user_objects]
	return list(map(int, user_ids))

def main():
	global original_df
	recover = False
	temp_df = get_latest_df("original_df")
	#print(len(temp_df) if temp_df is not None else "None")
	original_df = create_original_df() if temp_df is None else temp_df
	if len(original_df) != 0 :
		recover = True
		#print("recovering the system from the existing files")
	temp_df = get_latest_df("retweet")
	#print(len(temp_df) if temp_df is not None else "None")
	df = create_df() if temp_df is None else temp_df
	df['next_update'] = pd.to_datetime(df['next_update'])
	df['created_time'] = pd.to_datetime(df['created_time'])
	watcher_t = threading.Thread(target=bird_watcher, daemon=True)
	scheduler_t = threading.Thread(target=scheduler, daemon=True, kwargs={'df':df, 'recover':recover})
	watcher_t.start()
	scheduler_t.start()
	watcher_t.join()
	scheduler_t.join()
	

if __name__ == "__main__":
	# parser = argparse.ArgumentParser(description='Starting in recovery mode', argument_default=False)
	# parser.add_argument("--recover", type=lambda x:bool(util.strtobool(x)),choices=[True, False],
	# 		help="Setting this variable to true or false will enable or disable recovery mode")
	# args = parser.parse_args()
	# main(args['recover'])
	main()
