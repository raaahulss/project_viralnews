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

    def get_tweet_from_url(self, tweet_url):
        """
        Given a tweet url this method identifies the tweet id from the url
        and then queries get_tweet_from_id to return a tweet object.
        The URL must be of the form https://twitter.com/[user]/status/[tweet_id]
        or twitter.com/[user]/status/[tweet_id] 
        :error: malformed url, the application error "MAL_URL" is raised,
        :returns: tweet object
        """
        m = re.match("https://twitter.com/(.*)/status/(.*)", tweet_url)
        n = re.match("twitter.com/(.*)/status/(.*)", tweet_url)
        o = m or n
        if type(tweet_url) is str and o and o.group(2).isnumeric():
            return self.get_tweet_from_id(int(o.group(2)))
        else:
            raise ApplicationError(*error_list["MAL_URL"])
