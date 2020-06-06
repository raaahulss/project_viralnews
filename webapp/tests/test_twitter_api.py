import unittest
import pytest
import src.constants as constants
import tweepy
from src.collection.twitter_api import TwitterApi
from src.error import *


TWEET_ID = 1267366725588185091

def test_given_valid_keys_returns_valid_api():
    """
        given valid credentials this method checks whether system
        connects to the api correctly
    """
    try:
        api = TwitterApi(constants.CONSUMER_KEY,
                    constants.CONSUMER_SECRET,
                    constants.ACCESS_TOKEN_KEY,
                    constants.ACCESS_TOKEN_SECRET)
        assert type(api) is TwitterApi
    except ApplicationError:
        pytest.fail("Unexpected Error")
    



@pytest.mark.parametrize("consumer_key, consumer_secret",
[
    ("", constants.CONSUMER_SECRET, ),
    (constants.CONSUMER_KEY, "", ),
    (constants.CONSUMER_SECRET, constants.CONSUMER_KEY, )
] )
def test_given_invalid_keys_returns_error( consumer_key, consumer_secret):
    """
        given invalid consumer keys, the system generates an Application Error
    """
    with pytest.raises(ApplicationError) as error:
        api = TwitterApi(consumer_key,
                    consumer_secret,
                    constants.ACCESS_TOKEN_KEY,
                    constants.ACCESS_TOKEN_SECRET)

def test_given_valid_keys_returns_tweet():
    """
        given a valid API and a valid tweet_id the system returns
        a valid tweet object
    """
    api = TwitterApi(constants.CONSUMER_KEY,
                    constants.CONSUMER_SECRET, 
                    constants.ACCESS_TOKEN_KEY,
                    constants.ACCESS_TOKEN_SECRET)
    tweet = api.get_tweet_from_id(TWEET_ID)
    assert tweet.id == TWEET_ID


@pytest.mark.parametrize("token, secret, tweetid",
[
    # ("", "", TWEET_ID ),
    (constants.ACCESS_TOKEN_KEY, "", TWEET_ID),
    ("", constants.ACCESS_TOKEN_SECRET,TWEET_ID ),
    (constants.ACCESS_TOKEN_KEY, constants.ACCESS_TOKEN_SECRET, 12673667255881851212121091),
    # (None, None, TWEET_ID),
    (constants.ACCESS_TOKEN_KEY, constants.ACCESS_TOKEN_SECRET, None)
] )
def test_given_invalid_keys_or_tweetid_return_error(token, secret, tweetid):
    """
    Given invalid keys or invalid tweet id the system returns an error.
    Note: The commented line above is where the system does not generate an error
    """
    with pytest.raises(ApplicationError) as error:
        api = TwitterApi(constants.CONSUMER_KEY,
                    constants.CONSUMER_SECRET,
                    token,
                    secret)
        api.get_tweet_from_id(tweetid)

# TODO: Search for a way to rate limit exceed error check

@pytest.mark.parametrize("url, id",
[
    ("https://twitter.com/nytimes/status/1267366725588185091",1267366725588185091),
    ("twitter.com/nytimes/status/1267366725588185091",1267366725588185091),

])
def test_given_valid_url_returns_tweet_object(url, id):
    """
    given a valid tweet url, the method returns a tweet object
    """
    api = TwitterApi(constants.CONSUMER_KEY,
                    constants.CONSUMER_SECRET, 
                    constants.ACCESS_TOKEN_KEY,
                    constants.ACCESS_TOKEN_SECRET)
    tweet = api.get_tweet_from_url(url)
    assert tweet.id == id
    assert type(tweet) is tweepy.Status


@pytest.mark.parametrize("url",
[
    "https://twitter.com/home",
    "https://twitter.com/nytimes/status/1267366725588185091123123",
    "twitter.com/nytimes/status/1267366725588185091123123",
    "twitter.com/nytimes/status/asdasd",
]
)
def test_given_invalid_url_or_tweet_returns_error(url):
    api = TwitterApi(constants.CONSUMER_KEY,
                    constants.CONSUMER_SECRET, 
                    constants.ACCESS_TOKEN_KEY,
                    constants.ACCESS_TOKEN_SECRET)
    with pytest.raises(ApplicationError) as error:
        api.get_tweet_from_url(url)
