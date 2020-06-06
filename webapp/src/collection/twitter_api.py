import tweepy
from tweepy import TweepError, RateLimitError
from src.error import *
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
    def get_tweet(self, tweet_id):
        """
        given a valid twitter url, the method returns the tweet as a tweepy
        status object
        :error: malformed url, the application error "MAL_URL" is raised,
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

