from twarc import Twarc
import pandas as pd
import sys
import constants as cnst
import argparse

def main():
	parser = argparse.ArgumentParser(description='hydate tweets from file and write to new file')
	parser.add_argument('-f', required=True, help='CSV file to read tweet_id from')
	parser.add_argument('-o', required=True, help='CSV file to write out to')
	args = parser.parse_args()

	t = Twarc(cnst.consumer_key, cnst.consumer_secret,
			cnst.access_token, cnst.access_token_secret)
	df = pd.read_csv(args.f)


	# Add new columns
	df['user_id'] = -1
	df['screen_name'] = "name"
	df['url'] = "url"
	df['follower_count'] = -1


	# create list of tweet IDs from file
	tweet_ids = list()
	for row, index in df.iterrows():
	    tweet_ids.append(index["tweet_id"])


	print("\nHydrating Tweets...Please Wait....\n")

	# hydrate twitter IDs and add to df
	for tweet in t.hydrate(tweet_ids):
		df.loc[(df.tweet_id == tweet["id"]), "user_id"] = tweet["user"]["id"]
		df.loc[(df.tweet_id == tweet["id"]), "screen_name"] = tweet["user"]["name"]
		df.loc[(df.tweet_id == tweet["id"]), "follower_count"] = tweet["user"]["followers_count"]
		try:
			df.loc[(df.tweet_id == tweet["id"]), "url"] = tweet["entities"]["urls"][0]["expanded_url"]
		except:
			pass

	print("\nWriting to file...\n")

	df.to_csv(args.o)

if __name__ == "__main__":
	main()
