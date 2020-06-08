import tldextract
import validators
import pytest
from src.collection.twitter_api import get_tweet
from src.collection.news_fetcher import get_news
from src.error import ApplicationError, error_list

supported_sources=('twitter', 'nytimes', 'washingtonpost', 'wsj', 'cnn', 'nbcnews')

def preprocessor(url, publi):
    """
    Given a url, the preprocessor identifies the type of the url and generates
    news article data and/or twitter data. 
    
    :returns: Returns newsObject, tweeter object and error object
    """
    news, tweet, error = None, None, None
    source = ""
    if url is not None and not url.startswith("https://"):
        url = "https://" + url
       
    try:
        source = is_whitelisted_url(url)
    except ApplicationError as error:
        return (None, None, error)
    
    # if the 
    if source == "twitter":
        tweet, error = get_tweet(url)
        if error is not None:
            return (news, tweet, error)
    # in case
    news, error = get_news(tweet.expanded_url if source is "twitter" else url)
    
    if error is not None:
        return (news, tweet, error)
    
    return (news, tweet, error)

    # code for news media outlet.


def is_whitelisted_url(url):
    """
    Parse a given url to determine whether it is a valid url and whether the source is supported.
    :param url: A url given by user.
    :return: Return the source.
    :error: Application error if the source is not supported or invalid. 
    """
    
    if not validators.url(url):
        print('invalid url')
        raise ApplicationError(*error_list["MAL_URL"])

    _, source, _ = tldextract.extract(url)
    if source in supported_sources:
        # replace tldextract.extract(url).domain) with source
        # pytest.set_trace()
        return source
    else:
        print('unsupported source')
        raise ApplicationError(*error_list["UNSUP_SRC"])
        # return -1   # Error codes are not defined yet, use -1 for convenience