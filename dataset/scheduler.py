import csv
import pandas as pd
import datetime
import pytz

from random import seed
from random import randint

utc=pytz.UTC


# global dict definition
tweets = {}

def csv_reader():
	while(1):
		# read columns that we need from CSV
		col_list = ["tweet_id", "datetime_published", "current_retweets","article_URL", "handle"]
		df = pd.read_csv("sample_dataset.csv", usecols=col_list)

		# loop through dataframe. If tweet_id not in dict, add to dict
		for row,value in df.iterrows():
			if(value["tweet_id"] not in tweets.values()):
				datetimePublished = datetime.datetime.strptime(value["datetime_published"], '%a %b %d %H:%M:%S %z %Y')
				nextUpdate =  datetimePublished + datetime.timedelta(hours=24)
				tweets.update({row: {'tweet_id':value["tweet_id"], 
									 'datetime_published': datetimePublished, 
									 'next_update': nextUpdate,
									 'current_time': datetime.datetime.now(),
									 'current_retweets':value["current_retweets"],
									 'url': value["article_URL"],
									 'handle' : value["handle"],
									 'count':0}})
		sleep(10)


def scheduler():
	time_now = utc.localize(datetime.datetime.now())
	time_range = time_now + datetime.timedelta(minutes=1)
	
	for value in tweets.values():
		if value["next_update"] >= time_now and value["next_update"] <= time_range:
			curr_retweets = get_retweets(value["tweet_id"])
			# count starts at 0, so, we will increment by 1, and then write to that column
			value["count"] = value["count"] + 1
			#write curr_retweets to column "counter"
			#check if first time writing. If not first time, just need to write curr_retweets
			if(value["count"] == 1):
				data = { 'tweet_id':[value["tweet_id"]],
						 'url':[value["url"]],
						 'handle':[value["handle"]],
						 '1':[value["count"]]}

				df = pd.DataFrame(data, columns = ['tweet_id', 'url', 'handle', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])
				df.to_csv('sample_output.csv', index=False, na_rep='NULL', mode='a', header=False)
			else:
				df = pandas.read("sample_output.csv")
				df.loc[df.tweet_id == value["tweet_id"], value["count"]] = curr_retweets
				#update next update time by adding 24 hrs
				value["next_update"] = (value["next_update"] + datetime.timedelta(hours=24))


def get_retweets(tweet_id):
	seed(1)
	return (randint(10,1000))


def main():
	csv_reader()
	scheduler()



if __name__ == "__main__":
	main()
