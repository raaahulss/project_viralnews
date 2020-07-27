import tldextract
import validators
from src.collection.twitter_api import get_tweet
from src.collection.news_fetcher import get_news_from_url
from src.collection.news_fetcher import get_news_from_file
from src.error import ApplicationError, error_list

supported_sources = ('twitter', 'nytimes', 'wsj', 'cnn', 'nbcnews','latimes','npr','reuters','huffpost','abcnews')


def preprocessor(url, published):
    """
    Given a url(a web url or a file object), the preprocessor identifies 
    the type of the url and generates
    news article data and/or twitter data. 
    
    :returns: Returns newsObject, tweeter object and error object
    """
    news, tweet, error = None, None, None
    # article is published
    if published:
        if url is not None and not url.startswith("https://"):
            url = "https://" + url

        try:
            source = is_whitelisted_url(url)
        except ApplicationError as error:
            return None, None, error

        # if the url is from twitter
        if source == "twitter":
            tweet, error = get_tweet(url)
            if error is not None:
                return None, None, error
            # check expanded url to make sure it is supported
            try:
                is_whitelisted_url(tweet.expanded_url)
                news, error = get_news_from_url(tweet.expanded_url)
            except ApplicationError as error:
                error = ApplicationError(*error_list["UNSUP_EMB_URL"])
                return None, None, error
        else:
            news, error = get_news_from_url(url)

        if error is not None:
            return None, None, error
    # article is not published
    else:
        news, error = get_news_from_file(url)
        if error is not None:
            return None, None, error
    
    return news, tweet, error


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
