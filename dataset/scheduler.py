import csv
import pandas as pd
import datetime
import pytz
import time
import threading
from twarc import Twarc

from random import seed
from random import randint

utc=pytz.UTC


#TODO Think about how to structure sleeps in order to mimimize race conditions for access to tweets shared dict
#TODO add proper logging to log.txt

# Twitter keys 
consumer_key='58wlGpzEOwum6nghvA8tj6nz6'
consumer_secret='b04KqyzRyquIiYGwqv9B12hRqjEj9tvOp53DtoFZJtetaZ7cZE'
access_token='1243275961824612358-65qxIlXTEhjw0jlbBaK4I0olH9nRP9'
access_token_secret='wYdkYaNCakb7sX5PnHjF1u0oJc7Y73iijqbJ4VeB4yyEd'

# global twarc object
t = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

def bird_watcher():
	global original_df 
	columns = ["screen_name", "tweet_id","created_at","embeded_url","expanded_url","author","title",
	   "content", "day_0_time","day_0_retweet_count", "next_update", "count"]

	original_df = pd.DataFrame(columns=columns)
	parsed = 0
	
	follow_list = [759251,3108351,2467791,14173315,51241574,28785486,16664681,807095,5392522,14293310,6577642,15754281]
	follow_str = ",".join([str(x) for x in follow_list])

	start = time.time()
	print("Following users ",follow_str)
	for tweet in t.filter(follow=follow_str):
		parsed += 1
		if 'retweeted_status' not in tweet:
			try:
				if tweet['user']['id'] in follow_list \
				and len(tweet['entities']['urls']) != 0 \
				and (original_df['tweet_id'] != tweet['id']).all():
					current = datetime.datetime.now(datetime.timezone.utc)
					datetimePublished = datetime.datetime.strptime(tweet["created_at"], '%a %b %d %H:%M:%S %z %Y')
					nextUpdate =  datetimePublished + datetime.timedelta(hours=1)
					print("\nBIRDWATCHER \t Adding tweet From source", tweet['id'], "\tcreated_time: ", tweet['created_at'], "\tnext_update: ", nextUpdate)
					original_df = original_df.append({'screen_name':tweet['user']['screen_name'], 
							'tweet_id':tweet['id'],
							'created_at' : tweet['created_at'],
							'embeded_url' : tweet['entities']['urls'][0]['url'],
							'day_0_retweet_count': tweet['retweet_count'],
							'day_0_time': current,
							'next_update': nextUpdate,
							'count' : 0 }, ignore_index=True)
			except:
				print("\nBIRDWATCHER \t Error in conditional, tweet_id: ", tweet['id'])	
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
						datetimePublished = datetime.datetime.strptime(tweet["retweeted_status"]["created_at"], '%a %b %d %H:%M:%S %z %Y')
						nextUpdate =  datetimePublished + datetime.timedelta(hours=1)
						print("\nBIRDWATCHER \t From retweet", tweet['id'], "Adding tweet: ", tweet["retweeted_status"]["id"], "\tcreated_time: ", datetimePublished, "\tnext_update: ", nextUpdate)
						original_df = original_df.append({'screen_name':tweet["retweeted_status"]["user"]["screen_name"], 
							'tweet_id':tweet["retweeted_status"]["id"],
							'created_at' : tweet["retweeted_status"]["created_at"],
							'embeded_url' : tweet["retweeted_status"]["extended_tweet"]["entities"]["urls"][0]["url"],
							'day_0_retweet_count': tweet['retweeted_status']['retweet_count'],
							'day_0_time': current,
							'next_update': nextUpdate,
							'count' : 0 }, ignore_index=True)
			except:
				print("\nBIRDWATCHER \t Error in conditional, tweet_id: ", tweet['id'])	
				

def scheduler():
	global original_df

	column_names = ['tweet_id','url','handle','count','created_time','next_update']
	for i in range(1, 101):
		column_names.append(str(i))

	df = pd.DataFrame(columns = column_names)

	count=0
	while(1):
		# Run loop every 60s
		time.sleep(60)
		print("\nSCHEDULER\t loop starting...")

		# Time range is 2 minutes
		time_now = datetime.datetime.utcnow().replace(tzinfo=utc)
		time_range = time_now + datetime.timedelta(minutes=2)
        
		print("\nSCHEDULER\t", "time_now: ", time_now, " time_range: ", time_range)
		for row in original_df.itertuples():
			try:
				current_update = ((df.loc[(df.tweet_id == row.tweet_id), 'next_update'])[0])
			except:
				current_update = row.next_update
			if((row.next_update >= time_now and row.next_update <= time_range) or (current_update >= time_now and current_update <= time_range)):
				curr_retweets = get_retweets(row.tweet_id,t)
				if(not(row.tweet_id in df.tweet_id.values)):
					next_update = row.next_update + datetime.timedelta(hours=1)
					print("\nSCHEDULER\t ", row.tweet_id, " first time being added\t create_time: ", row.created_at, "\tnext_update: ", next_update)
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
					current_count = (df.loc[(df.tweet_id == row.tweet_id), 'count'])[0]
					df.loc[(df.tweet_id == row.tweet_id), str(current_count)] = curr_retweets
					current_update = ((df.loc[(df.tweet_id == row.tweet_id), 'next_update'])[0])
					new_time = current_update + datetime.timedelta(hours=1)
					print("\nSCHEDULER\t ", row.tweet_id, " updating retweets for offfset # ", current_count, 
						  "created_time: ", row.created_at, "\tcurrent_update: ", current_update, "\tnew_update: ", new_time)
					df.loc[(df.tweet_id == row.tweet_id), 'next_update'] = new_time
					df.loc[(df.tweet_id == row.tweet_id), 'count'] = (int(current_count) + 1)
					count= count + 1

				# write to file when 25 tweets have been updated/added
				if(count >=25):
					df.to_csv('sample_output.csv', index=True)
					count = 0

def get_retweets(tweet_id, twarc_api):
	for tweet in twarc_api.hydrate([tweet_id]):
		return tweet['retweet_count']

def main():
	watcher_t = threading.Thread(target=bird_watcher, daemon=True)
	scheduler_t = threading.Thread(target=scheduler, daemon=True)
	watcher_t.start()
	scheduler_t.start()
	watcher_t.join()
	scheduler_t.join()

if __name__ == "__main__":
	main()
