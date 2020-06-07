import tweepy
from tweepy import TweepError, RateLimitError
from src.error import *
import re
class TwitterApi(object):

    def __init__(self, consumer_key, consumer_secret, access_token_key="", access_token_secret=""):
        """
        This method authenticates and creates a twitterapi object.
        In case the system is unable to authenticate the object, a SystemError is returned.
        """
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        try:
            auth.get_authorization_url()
        except TweepError as e:
            print("Unable to authenticate", str(e))
            raise ApplicationError(*error_list["AUTH_ERROR"])
        
        auth.set_access_token(access_token_key, access_token_secret)
        self._api = tweepy.API(auth_handler=auth)

    # @property
    def get_tweet_from_id(self, tweet_id):
        """
        given a valid twitter url, the method returns the tweet as a tweepy
        status object
        :error: in case of limit reached "RT_LMT_RCHD" is raised
        :returns: tweet object 
        """
        try:
            tweet = self._api.get_status(tweet_id, tweet_mode="extended")
            return tweet
        except RateLimitError as r:
            print("Rate limit exceeded", str(r))
            raise ApplicationError(*error_list["RT_LMT_RCHD"])
        except TweepError as e:
            print("Error occured", str(e))
            raise ApplicationError(*error_list["FTCH_ERR"])

    def _is_valid_url(self, tweet_url):
        m = re.match("https://twitter.com/(.*)/status/(.*)", tweet_url)
        n = re.match("twitter.com/(.*)/status/(.*)", tweet_url)
        o = m or n
        return o
    
    def get_tweet_from_url(self, tweet_url):
        """
        Given a tweet url this method identifies the tweet id from the url
        and then queries get_tweet_from_id to return a tweet object.
        The URL must be of the form https://twitter.com/[user]/status/[tweet_id]
        or twitter.com/[user]/status/[tweet_id] 
        :error: malformed url, the application error "MAL_TWT_URL" is raised,
        :returns: tweet object
        """
        o = self._is_valid_url(tweet_url)
        if type(tweet_url) is str and o and o.group(2).isnumeric():
            return self.get_tweet_from_id(int(o.group(2)))
        else:
            raise ApplicationError(*error_list["MAL_TWT_URL"])
    
    def get_original_tweet_from_url(self,tweet_url):
        """
        Given a url this method returns the source twitter object of the tweet.
        That is, if a tweet A is a retweet, this method returns the source tweet B
        for retweet A or if the tweet A is  source tweet, it returns tweet A.
        The system is coded with assumption that there can be retweets or a retweet,
        hence this method searches the original tweet by looping over and over
        till the "in_reply_to_status_id_str" is None"
        """
        original_tweet, tweet = None, None
        while(True):
            # if tweet is None then this is first call and we use the tweet_url
            if tweet is None:
                tweet = self.get_tweet_from_url(tweet_url)
                print("Got tweet with id", tweet.id)
            print("Type of obj", type(tweet))
            if tweet.in_reply_to_status_id_str is None:
                original_tweet = tweet
                break
            else:
                tweet = self.get_tweet_from_id(tweet.in_reply_to_status_id)
        return original_tweet