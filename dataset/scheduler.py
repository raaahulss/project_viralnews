import csv
import pandas as pd
import datetime
import pytz
import time
import threading

from random import seed
from random import randint

utc=pytz.UTC


#TODO add G's code as a library
#TODO Think about how to structure sleeps in order to mimimize race conditions for access to tweets shared dict
#TODO add proper logging to log.txt

# global dict definition
tweets = {}

#TODO CHANGE to use pandas df from G's code
def csv_reader():
    print("\n Reader Thread Started....\n")
    while(1):
        # read columns that we need from CSV
        col_list = ["tweet_id", "datetime_published", "current_retweets","article_URL", "handle"]
        df = pd.read_csv("sample_dataset.csv", usecols=col_list)

        # loop through dataframe. If tweet_id not in dict, add to dict
        for row,value in df.iterrows():
            #print(tweets)
            if(not(any(value["tweet_id"] in d.values() for d in tweets.values()))):
                datetimePublished = datetime.datetime.strptime(value["datetime_published"], '%a %b %d %H:%M:%S %z %Y')
                #TODO CHANGE timedelta to hours=24
                nextUpdate =  datetimePublished + datetime.timedelta(minutes=3)
                print("\nREADER\t", "Adding new tweet to tweets dict, tweet ID: ", value["tweet_id"], "datetime_pub: ", datetimePublished, " next update: ", nextUpdate)
                tweets.update({row: {'tweet_id':value["tweet_id"], 
                                                     'datetime_published': datetimePublished, 
                                                     'next_update': nextUpdate,
                                                     'current_time': datetime.datetime.now(),
                                                     'current_retweets':value["current_retweets"],
                                                     'url': value["article_URL"],
                                                     'handle' : value["handle"],
                                                     'count':0}})
        time.sleep(30)


def scheduler():
    print("\n Scheduler Thread Started....\n")
    

    retweets = {}
    column_names = ['tweet_id','url','handle']
    for i in range(1, 101):
        column_names.append(str(i))

    df = pd.DataFrame(columns = column_names)
    
    count=0
    #writes=0

    while(1):
        time.sleep(30)
        time_now = datetime.datetime.utcnow().replace(tzinfo=utc)
        time_range = time_now + datetime.timedelta(minutes=1)
        
        print("\nSCHEDULER\t", "time_now: ", time_now, " time_range: ", time_range)
        
        for value in tweets.values():
            print("\nSCHEDULER\t", "next_update: ", value["next_update"])
            if value["next_update"] >= time_now and value["next_update"] <= time_range:
                print("\n", value["tweet_id"], " is in time range")
                curr_retweets = get_retweets(value["tweet_id"])
                # count starts at 0, so, we will increment by 1, and then write to that column
                value["count"] = value["count"] + 1
                #write curr_retweets to column "counter"
                #check if first time writing. If not first time, just need to write curr_retweets
                if(value["count"] == 1):
                    print("\n", value["tweet_id"], " first time being added")
                    data = { 'tweet_id':[value["tweet_id"]],
                             'url':[value["url"]],
                             'handle':[value["handle"]],
                             '1':[curr_retweets]}

                    df_temp = pd.DataFrame(data, columns=column_names)
                    df = df.append(df_temp).fillna(-1)
                    print("\n dataframe after apend: ", df)
                    #TODO CHANGE timedelta to hours=24
                    value["next_update"] = (value["next_update"] + datetime.timedelta(minutes=3))
                    count = count + 1
                else:
                    print("\n", value["tweet_id"], " updating retweets for offset # ", value["count"])
                    df.loc[(df.tweet_id == value["tweet_id"]), str(value["count"])] = curr_retweets
                    #update next update time by adding 24 hrs
                    #TODO CHANGE timedelta to hours=24
                    value["next_update"] = (value["next_update"] + datetime.timedelta(minutes=3))
                    count= count + 1

                #TODO CHANGE count to something higher based off testing
                if(count >=5):
                    df.to_csv('sample_output.csv', index=True, na_rep='NULL')
                    count = 0

#TODO Implement the hydrate function from G's code
def get_retweets(tweet_id):
        return (randint(10,1000))


def main():
        reader_t = threading.Thread(target=csv_reader, daemon=True)
        scheduler_t = threading.Thread(target=scheduler, daemon=True)
        reader_t.start()
        scheduler_t.start()
        reader_t.join()
        scheduler_t.join()


if __name__ == "__main__":
        main()
