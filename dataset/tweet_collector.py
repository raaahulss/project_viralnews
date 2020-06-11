import pandas as pd
import datetime
import pytz
import time
import threading
from twarc import Twarc
import os
import tweepy

utc=pytz.UTC

# Twitter keys 
consumer_key='58wlGpzEOwum6nghvA8tj6nz6'
consumer_secret='b04KqyzRyquIiYGwqv9B12hRqjEj9tvOp53DtoFZJtetaZ7cZE'
access_token='1243275961824612358-65qxIlXTEhjw0jlbBaK4I0olH9nRP9'
access_token_secret='wYdkYaNCakb7sX5PnHjF1u0oJc7Y73iijqbJ4VeB4yyEd'

# global twarc object
t = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

# This thread monitors the twitter accounts
def bird_watcher():
	global original_df 
	
# Delete old log file and create new one
	if os.path.exists("bird_watcher.log"):
		os.remove("bird_watcher.log")
	bird_log = open("bird_watcher.log", "a")

	columns = ["screen_name", "tweet_id","created_at","embeded_url","expanded_url","author","title",
					 	 "content", "day_0_time","day_0_retweet_count", "next_update", "count"]
	
	original_df = pd.DataFrame(columns=columns)

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
					nextUpdate =  datetimePublished + datetime.timedelta(hours=1)
					log = str("\n[" + str(current) + "] BIRDWATCHER \t Adding tweet From source "+str( tweet['id'])+"\tcreated_time: "+str(datetimePublished)+"\tnext_update: "+str(nextUpdate))
					print(log)
					bird_log.write(log)
					bird_log.flush()
					original_df = original_df.append({'screen_name':tweet['user']['screen_name'], 
							'tweet_id':tweet['id'],
							'created_at' : tweet['created_at'],
							'embeded_url' : tweet['entities']['urls'][0]['url'],
							'day_0_retweet_count': tweet['retweet_count'],
							'day_0_time': current,
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
						nextUpdate =  datetimePublished + datetime.timedelta(hours=1)
						log = str("\n[" + str(current) + "] BIRDWATCHER \t From retweet "+str(tweet['id'])+" Adding tweet: "+str(tweet["retweeted_status"]["created_at"])+ "\tcreated_time: "+str(datetimePublished)+"\tnext_update: "+str( nextUpdate))
						print(log)
						bird_log.write(log)
						bird_log.flush()
						original_df = original_df.append({'screen_name':tweet["retweeted_status"]["user"]["screen_name"], 
							'tweet_id':tweet["retweeted_status"]["id"],
							'created_at' : tweet["retweeted_status"]["created_at"],
							'embeded_url' : tweet["retweeted_status"]["extended_tweet"]["entities"]["urls"][0]["url"],
							'day_0_retweet_count': tweet['retweeted_status']['retweet_count'],
							'day_0_time': current,
							'next_update': nextUpdate,
							'count' : 0 }, ignore_index=True)
			except:
				current = datetime.datetime.now(datetime.timezone.utc)
				log = str("\n[" + str(current) + "] BIRDWATCHER \t Error in conditional")
				print(log)
				bird_log.write(log)
				bird_log.flush()
				
# This thread is responsible for getting the retweets every 24 hrs
def scheduler():
	global original_df

	if os.path.exists("scheduler.log"):
  		os.remove("scheduler.log")
	scheduler_log = open("scheduler.log", "a")

	column_names = ['tweet_id','url','handle','count','created_time','next_update']
	for i in range(1, 101):
		column_names.append(str(i))

	df = pd.DataFrame(columns = column_names)

	count=0
	start_time = time.time()
	while(1):
		time.sleep(30)

		# Time range is 2 minutes
		time_now = datetime.datetime.utcnow().replace(tzinfo=utc)
		time_range = time_now + datetime.timedelta(minutes=2)
        
		log = str("\n["+str(time_now) + "] SCHEDULER \t Loop starting \t time_now: "+str(time_now)+"\ttime_range: "+str(time_range))
		print(log)
		scheduler_log.write(log)
		scheduler_log.flush()
		for row in original_df.itertuples():
			try:
				current_update = ((df.loc[(df.tweet_id == row.tweet_id), 'next_update'])[0])
			except:
				current_update = row.next_update
			if((row.next_update >= time_now and row.next_update <= time_range) or (current_update >= time_now and current_update <= time_range)):
				curr_retweets = get_retweets(row.tweet_id,t)
				if(not(row.tweet_id in df.tweet_id.values)):
					next_update = row.next_update + datetime.timedelta(hours=1)
					current_time = datetime.datetime.utcnow().replace(tzinfo=utc)
					log=str("\n[" + str(current_time)+"] SCHEDULER\t "+str(row.tweet_id)+" first time being added\t create_time: "+str(row.created_at)+"\tcurrent update: " + str(row.next_update)+"\tnext_update: "+str(next_update))
					print(log)
					scheduler_log.write(log)
					scheduler_log.flush()
					data = { 'tweet_id':[row.tweet_id],
							 'url':[row.embeded_url],
							 'handle':[row.screen_name],
							 'count' : 2,
							 'created_time': [row.created_at],
							 'next_update' : [next_update],
							 '1':[curr_retweets]}
					df_temp = pd.DataFrame(data, columns=column_names)
					df = df.append(df_temp).fillna(-1)
					count = count + 1
				else:
					current_update = ((df.loc[(df.tweet_id == row.tweet_id), 'next_update'])[0])
					if(current_update >= time_now and current_update <= time_range):
						current_count = (df.loc[(df.tweet_id == row.tweet_id), 'count'])[0]
						df.loc[(df.tweet_id == row.tweet_id), str(current_count)] = curr_retweets
						new_time = current_update + datetime.timedelta(hours=1)
						current_time = datetime.datetime.utcnow().replace(tzinfo=utc)
						log=str("\n[" + str(current_time)+"] SCHEDULER\t "+str(row.tweet_id)+" update retweets for offset: " +str(current_count)+ "\t create_time: "+str(row.created_at)+"\tcurrent update: " + str(current_update)+"\tnext_update: "+str(new_time))
						print(log)
						scheduler_log.write(log)
						scheduler_log.flush()
						df.loc[(df.tweet_id == row.tweet_id), 'next_update'] = new_time
						df.loc[(df.tweet_id == row.tweet_id), 'count'] = (int(current_count) + 1)
						count= count + 1

		elapsed_time = time.time() - start_time
		#print("\n SCHEDULER \t start_time: ", start_time, "\telapsed: ", elapsed_time)
		if(elapsed_time >= 900):
			log=str("\n["+str(datetime.datetime.utcnow().replace(tzinfo=utc))+"] SCHEDULER\t Writing to file")
			print(log)
			scheduler_log.write(log)
			scheduler_log.flush()
			df.to_csv('data.csv', index=True)
			start_time = time.time()

		log=str("\n["+str(datetime.datetime.utcnow().replace(tzinfo=utc))+"] SCHEDULER\t Loop ending")
		print(log)
		scheduler_log.write(log)
		scheduler_log.flush()

def get_retweets(tweet_id, twarc_api):
	for tweet in twarc_api.hydrate([tweet_id]):
		return tweet['retweet_count']


# convert handles to user_ids
def get_userIds():

	# create Tweepy object
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
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
	watcher_t = threading.Thread(target=bird_watcher, daemon=True)
	scheduler_t = threading.Thread(target=scheduler, daemon=True)
	watcher_t.start()
	scheduler_t.start()
	watcher_t.join()
	scheduler_t.join()

if __name__ == "__main__":
	main()
