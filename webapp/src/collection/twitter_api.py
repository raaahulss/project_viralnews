import tweepy
import re
from tweepy import TweepError, RateLimitError
from src.error import *
import src.constants as cnst
import pytest
import requests
from datetime import datetime
from twarc import Twarc
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
        try:
            self._api_twarc = Twarc(cnst.CONSUMER_KEY, cnst.CONSUMER_SECRET, cnst.ACCESS_TOKEN_KEY, cnst.ACCESS_TOKEN_SECRET)
        except Exception as e:
            print("Unable to authenticate", str(e))
            raise ApplicationError(*error_list["AUTH_ERROR"])

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
            raise ApplicationError(*error_list["LMT_RCHD_ERROR"])
        except TweepError as e:
            print("Error occured", str(e))
            raise ApplicationError(*error_list["FTCH_ERR"])

    def _is_valid_url(self, tweet_url):
        url_without_share = tweet_url.split("?")[0]
        m = re.match("https://twitter.com/(.*)/status/(.*)", url_without_share)
        n = re.match("twitter.com/(.*)/status/(.*)", url_without_share)
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
        :error: Application error if there is no embeded url
        :error: Application error if the original tweet is older than 7 or 30 days,
                depending on the end
        """
        original_tweet, tweet = None, None
        while True:
            # if tweet is None then this is first call and we use the tweet_url
            if tweet is None:
                tweet = self.get_tweet_from_url(tweet_url)
            if not tweet.is_quote_status:
                # is_quote_status is false for original tweet 
                original_tweet = tweet
                break
            # if tweet.in_reply_to_status_id_str is None:
            #     original_tweet = tweet
            #     # pytest.set_trace()
            #     break
            else:
                tweet = self.get_tweet_from_id(tweet.quoted_status_id)
                # tweet = self.get_tweet_from_id(tweet.in_reply_to_status_id)
        if len(original_tweet.entities["urls"]) == 0:
            raise ApplicationError(*error_list["NO_EMBD_URL"])
        if (original_tweet.created_at - datetime.now()).days >= cnst.MAX_TWEET_CREATION_RANGE:
            # pytest.set_trace()
            raise ApplicationError(*error_list["EXPRD_TWT"])
        return original_tweet

    def get_replies(self, tweet, reply_limit=cnst.MAX_REPLY, search_per_request=cnst.SEARCH_PER_REQUEST):
        """
        This method takes in the tweet object and returns replies
        for the tweet, the count of replies are defined by reply_limit.
        :error: AssertionError if the tweet object is not of type Tweepy.status
        :error: Application Error if the limit for the twitter API is reached.
        """
        assert type(tweet) == tweepy.Status
        reply_tweet_ids_list = list()
        # get replies on the original tweet
        self.get_reply_ids_(tweet, reply_limit, search_per_request, reply_tweet_ids_list)
        # self.get_reply_ids(tweet, reply_limit, search_per_request, reply_tweet_ids_list)
        
        # in case the list is not big enough get replies to the reply tweets
        # until limit is reached. We do not go deeper that level 1 tweet.
        # NOTE: Commenting below code as we are not going deeper than level one.
        # if len(reply_tweet_ids_list) < reply_limit:
        #     temp_list = reply_tweet_ids_list.copy()
        #     for tweet_id in temp_list:
        #         tweet = api.get_tweet_from_id(tweet_id)
        #         self.get_reply_ids(tweet, reply_limit, search_per_request, reply_tweet_ids_list)
        #         if len(reply_tweet_ids_list) < reply_limit:
        #             break
        
        # get comments from the list
        replies = list()
        for tweet in self._api_twarc.hydrate(reply_tweet_ids_list):
            try:
                replies.append(tweet['full_text'])
            except Exception as e:
                print(str(e))

        # for reply_id in reply_tweet_ids_list:
        #     tweet = self.get_tweet_from_id(reply_id)
        #     try:
        #         replies.append(tweet.retweeted_status.full_text)
        #     except AttributeError:  # Not a Retweet should never occur
        #         replies.append(tweet.full_text)
        return replies

    def get_reply_ids_(self, tweet, reply_limit, search_per_request, reply_tweet_ids_list):
        """
        Given a tweet this method returns a list of ids for the retweets with comments using the premium api.
        :error: Applicaiton Error when limit is reached.
        :error: Assertion Error if the reply_tweet_ids_list is None or not a list
        """
        assert reply_tweet_ids_list is not None
        assert type(reply_tweet_ids_list) == list
        tweet_id = tweet.id
        user_name = tweet.user.screen_name
        search_string = "url:https%3A%2F%2Ftwitter.com%2F{}%2Fstatus%2F{} lang:en".format(user_name, tweet_id)
        replies = tweepy.Cursor(self._api.search_30_day,cnst.SEARCH_ENV,search_string, maxResults=search_per_request).items()
        try:
            startTime = datetime.now()
            for reply in replies:
                current_time = datetime.now()
                if reply.is_quote_status and reply.quoted_status.id ==tweet.id:
                    reply_tweet_ids_list.append(reply.id)
                if len(reply_tweet_ids_list) == reply_limit or \
                     (current_time-startTime).total_seconds() >= cnst.MAX_TIME_REPLY_SEARCH :
                    break
            print("Returning",len(reply_tweet_ids_list), " replies")
            return reply_tweet_ids_list
        except tweepy.TweepError as e:
            raise ApplicationError(*error_list["LMT_RCHD_ERROR"])
        

                
    def get_reply_ids(self, tweet, reply_limit, search_per_request, reply_tweet_ids_list):
        """
        given a tweet this method returns list of reply tweet ids for the given tweet.
        The upper limit for the tweets returned is defined by reply_limit
        :error: Applicaiton Error when limit is reached.
        :error: Assertion Error if the reply_tweet_ids_list is None or not a list
        """
        # reply_tweet_ids = list()
        assert reply_tweet_ids_list is not None
        assert type(reply_tweet_ids_list) == list
        tweet_id = tweet.id
        user_name = tweet.user.screen_name
        max_id = None
        replies = tweepy.Cursor(self._api.search, count=search_per_request,
                                q='to:{}'.format(user_name),
                                since_id=tweet_id, max_id=max_id,
                                tweet_mode='extended').items()
        
        try:
            startTime = datetime.now()
            for reply in replies:
                current_time = datetime.now()
                if(reply.in_reply_to_status_id == tweet_id):
                    # pytest.set_trace()
                    reply_tweet_ids_list.append(reply.id)
                if len(reply_tweet_ids_list) == reply_limit or \
                     (current_time-startTime).total_seconds() >= cnst.MAX_TIME_REPLY_SEARCH :
                    # pytest.set_trace()
                    break
                max_id = reply.id
            # pytest.set_trace()
            return reply_tweet_ids_list
        except tweepy.TweepError as e:
            raise ApplicationError(*error_list["LMT_RCHD_ERROR"])


class Tweet:
    def __init__(self, tweet, responses):
        self.tweet_id = tweet.id
        self.retweet_count = tweet.retweet_count
        self.favorite_count = tweet.favorite_count
        self.responses = responses
        self.responses_count = len(responses)
        self.embeded_url = tweet.entities["urls"][0]["url"]
        http = requests.Session()
        http.headers.update({'User-Agent': 'newspaper/0.2.8',
                            'Accept-Encoding': 'gzip, deflate',
                            'Accept': '*/*',
                            'Connection': 'keep-alive'})
        try:
            resp = http.get(tweet.entities["urls"][0]["url"], timeout=cnst.REQUEST_TIME_OUT)
        except Exception:
            raise ApplicationError(*error_list["TIME_OUT"]) 

        # resp = requests.get(tweet.entities["urls"][0]["url"])
        self.expanded_url = resp.url
        # self.trending = trending

    def to_dict(self):
        return {"retweets": self.retweet_count,
                "favourites": self.favorite_count,
                "responses": self.responses_count,}
                # "trending": self.trending}

def get_tweet(tweet_url):
    """
    given a twitter url this method returns original tweet object and error object
    if the method recieves an error tweet object is set to None
    if things are processor successfully it returns tweet object and error object
    as None
    """
    try:
        api = TwitterApi(cnst.CONSUMER_KEY, cnst.CONSUMER_SECRET,
                         cnst.ACCESS_TOKEN_KEY, cnst.ACCESS_TOKEN_SECRET)
        # tweet = api.get_tweet_from_url(url)
        original_tweet = api.get_original_tweet_from_url(tweet_url)
        responses = api.get_replies(original_tweet)
        return Tweet(original_tweet, responses), None
    except ApplicationError as err:
        return None, err