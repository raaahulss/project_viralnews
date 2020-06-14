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
		print("Existing dataset not found for ", name)
		return None
	try:
		files_time = [(path.getctime(file), file) for file in files]
	except OSError as err:
		print("Existing dataset not found for ", name)
		print(str(err))
		return None
	files_time.sort(key=itemgetter(0), reverse=True)
	print("Existing dataset found for ", name, "returning", files_time[0][1])
	return pd.read_csv(files_time[0][1])

def export_dataset(df,name):
    name = "{}/{}_{}.csv".format(cnst.dataset_root_path,
					name, 
					datetime.datetime.now().strftime("%B_%d_%y_%H"))
    df.to_csv(name)

def create_original_df():
	columns = [
		# "screen_name",
		"tweet_id",
		"created_at",
		# "embeded_url",
		# "expanded_url",
		# "author",
		# "title",
 		# "content",
		# "day_0_time",
		# "day_0_retweet_count",
		"next_update",
		"count"]
	
	df = pd.DataFrame(columns=columns)
	return df

def create_df():
	column_names = ['tweet_id',
					# 'url',
					# 'handle',
					'count',
					'created_time',
					'next_update']
	for i in range(1, 101):
		column_names.append(str(i))

	df = pd.DataFrame(columns = column_names)
	return df



# This thread monitors the twitter accounts
def bird_watcher():
	global original_df 
	
# Delete old log file and create new one
	if os.path.exists("bird_watcher.log"):
		os.remove("bird_watcher.log")
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
					nextUpdate =  datetimePublished + datetime.timedelta(minutes=5)
					log = str("\n[" + str(current) + "] BIRDWATCHER \t Adding tweet From source "+str( tweet['id'])+"\tcreated_time: "+str(datetimePublished)+"\tnext_update: "+str(nextUpdate))
					print(log)
					bird_log.write(log)
					bird_log.flush()
					original_df = original_df.append({
						# 'screen_name':tweet['user']['screen_name'], 
							'tweet_id':tweet['id'],
							'created_at' : tweet['created_at'],
							# 'embeded_url' : tweet['entities']['urls'][0]['url'],
							# 'day_0_retweet_count': tweet['retweet_count'],
							# 'day_0_time': current,
							'next_update': nextUpdate,
							'count' : 0 }, ignore_index=True)
			except:
				current = datetime.datetime.now(datetime.timezone.utc)
				log = str("\n[" + str(current) + "] BIRDWATCHER \t Error in conditional")
				print(log)
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
						nextUpdate =  datetimePublished + datetime.timedelta(minutes=5)
						log = str("\n[" + str(current) + "] BIRDWATCHER \t From retweet "+str(tweet['id'])+" Adding tweet: "+str(tweet["retweeted_status"]["created_at"])+ "\tcreated_time: "+str(datetimePublished)+"\tnext_update: "+str( nextUpdate))
						print(log)
						bird_log.write(log)
						bird_log.flush()
						original_df = original_df.append({
							# 'screen_name':tweet["retweeted_status"]["user"]["screen_name"], 
							'tweet_id':tweet["retweeted_status"]["id"],
							'created_at' : tweet["retweeted_status"]["created_at"],
							# 'embeded_url' : tweet["retweeted_status"]["extended_tweet"]["entities"]["urls"][0]["url"],
							# 'day_0_retweet_count': tweet['retweeted_status']['retweet_count'],
							# 'day_0_time': current,
							'next_update': nextUpdate,
							'count' : 0 }, ignore_index=True)
			except:
				current = datetime.datetime.now(datetime.timezone.utc)
				log = str("\n[" + str(current) + "] BIRDWATCHER \t Error in conditional")
				print(log)
				bird_log.write(log)
				bird_log.flush()
				
# This thread is responsible for getting the retweets every 24 hrs
def scheduler(df, recover):
	global original_df
	print("original_df columns :", original_df.columns)
	print("df columns :", df.columns)
	if os.path.exists("scheduler.log"):
  		os.remove("scheduler.log")
	scheduler_log = open("scheduler.log", "a")

	column_names = ['tweet_id',
					# 'url',
					# 'handle',
					'count',
					'created_time',
					'next_update']
	for i in range(1, 101):
		column_names.append(str(i))
	
	start_time = time.time()
	while(1):
		time.sleep(60)

		# Time range is 2 minutes
		time_now = datetime.datetime.utcnow().replace(tzinfo=utc)
		time_range = time_now + datetime.timedelta(minutes=10)
		time_travel = time_now - datetime.timedelta(minutes=10)
        
		log = str("\n["+str(time_now) + "] SCHEDULER \t Loop starting \t time_now: "+str(time_now)+"\ttime_range: "+str(time_range))
		print(log)
		scheduler_log.write(log)
		scheduler_log.flush()
		print("Original DF length from scheduler ",len(original_df))
		# A list of (tweet_id)
		retweetables = list()
		for row in original_df.itertuples():
			try:
				current_update = pd.to_datetime((df.loc[(df.tweet_id == row.tweet_id), 'next_update'])[0])
			except:
				current_update = pd.to_datetime(row.next_update)
			
			if current_update >= time_travel and current_update <= time_range :
				retweetables.append(row.tweet_id)
		
		curr_retweets = get_retweets(retweetables,t)
		for retweetable_id  in retweetables:
			row = original_df.loc[original_df['tweet_id']==retweetable_id]
			print(row.tweet_id, retweetable_id)
			if(not(row.tweet_id in df.tweet_id.values)):
				next_update = pd.to_datetime(row.next_update) + datetime.timedelta(minutes=5)
				current_time = datetime.datetime.utcnow().replace(tzinfo=utc)
				log=str("\n[" + str(current_time)+"] SCHEDULER\t "+str(row.tweet_id)+" first time being added\t create_time: "+str(row.created_at)+"\tcurrent update: " + str(row.next_update)+"\tnext_update: "+str(next_update))
				print(log)
				scheduler_log.write(log)
				scheduler_log.flush()
				data = { 'tweet_id':[row.tweet_id],
						#  'url':[row.embeded_url],
						#  'handle':[row.screen_name],
							'count' : 2,
							'created_time': [row.created_at],
							'next_update' : [next_update],
							'1':[curr_retweets[row.tweet_id]]}
				df_temp = pd.DataFrame(data, columns=column_names)
				df = df.append(df_temp).fillna(-1)
			else:
				current_update = ((df.loc[(df.tweet_id == row.tweet_id), 'next_update'])[0])
				# if(current_update >= time_now and current_update <= time_range):
				current_count = (df.loc[(df.tweet_id == row.tweet_id), 'count'])[0]
				df.loc[(df.tweet_id == row.tweet_id), str(current_count)] = curr_retweets[row.tweet_id]
				new_time = current_update + datetime.timedelta(minutes=5)
				current_time = datetime.datetime.utcnow().replace(tzinfo=utc)
				log=str("\n[" + str(current_time)+"] SCHEDULER\t "+str(row.tweet_id)+" update retweets for offset: " +str(current_count)+ "\t create_time: "+str(row.created_at)+"\tcurrent update: " + str(current_update)+"\tnext_update: "+str(new_time))
				print(log)
				scheduler_log.write(log)
				scheduler_log.flush()
				df.loc[(df.tweet_id == row.tweet_id), 'next_update'] = new_time
				df.loc[(df.tweet_id == row.tweet_id), 'count'] = (int(current_count) + 1)

				
		elapsed_time = time.time() - start_time
		#print("\n SCHEDULER \t start_time: ", start_time, "\telapsed: ", elapsed_time)
		if(elapsed_time >= 120):
			log=str("\n["+str(datetime.datetime.utcnow().replace(tzinfo=utc))+"] SCHEDULER\t Writing to file")
			print(log)
			scheduler_log.write(log)
			scheduler_log.flush()
			log=str("\n["+str(datetime.datetime.utcnow().replace(tzinfo=utc))+"] SCHEDULER\t Original Frame len : "+str(len(original_df))+ "Data Frame len : "+str(len(df)))
			print(log)
			scheduler_log.write(log)
			scheduler_log.flush()
			if len(df) != 0:
				export_dataset(df, "retweet")
			if len(original_df) != 0:
				export_dataset(original_df, "original_df")
			# df.to_csv('data.csv', index=True)
			start_time = time.time()

		log=str("\n["+str(datetime.datetime.utcnow().replace(tzinfo=utc))+"] SCHEDULER\t Loop ending")
		print(log)
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
	print(len(temp_df) if temp_df is not None else "None")
	original_df = create_original_df() if temp_df is None else temp_df
	if len(original_df) != 0 :
		recover = True
		print("recovering the system from the existing files")
	temp_df = get_latest_df("retweet")
	print(len(temp_df) if temp_df is not None else "None")
	df = create_df() if temp_df is None else temp_df
	# df['next_update'] = pd.to_datetime(df['next_update'])
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
