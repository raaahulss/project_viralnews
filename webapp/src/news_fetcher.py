import tldextract
import validators
from newspaper import Article, ArticleException
from datetime import datetime

supported_sources=('twitter', 'nytimes', 'washingtonpost', 'wsj', 'cnn', 'nbcnews')


def parse_url(url):
    """Parse a given url to determine whether it is a valid url and whether the source is supported.

    Args:
        url: A url given by user.

    Returns:
        Return error code if the source is not supported or invalid. Return the source otherwise.
    """
    if not validators.url(url):
        print('invalid url')
        return -1

    _, source, _ = tldextract.extract(url)
    if tldextract.extract(url).domain in supported_sources:
        return source
    else:
        print('unsupported source')
        return -1   # Error codes are not defined yet, use -1 for convenience


class NewsObject(object):
    """News article base class

    """
    def __init__(self, url):
        self.url = url
        self.title = ''
        self.published_date = ''
        self.authors = ''
        self.content = ''
        self.error = False
        self.error_code = ''

    def fetch(self):
        article = Article(url)
        try:
            article.download()
            article.parse()
            self.title = article.title
            self.published_date = datetime.timestamp(article.publish_date)
            self.authors = article.authors
            self.content = article.text
        except ArticleException:
            self.error = True
            self.error_code = "connection_error"

    def to_dict(self):
        return {'metadata': {'error': self.error,
                             'error_code': self.error_code},
                'details': {'title': self.title,
                            'authors': self.authors,
                            'published_date': self.published_date,
                            'content': self.content,
                            'url': self.url}}


if __name__ == '__main__':
    # url = 'https://www.nytimes.com/2020/05/30/us/george-floyd-minneapolis.html?action=click&module=Spotlight&pgtype=Homepage'
    url = 'https://www.washingtonpost.com/technology/2020/05/30/spacex-nasa-launch-live-updates/'
    # url = 'https://www.cnn.com/us/live-news/george-floyd-protests-06-02-20/h_b7545fe33352aa03273bb774c926444a'
    # url = 'https://www.nbcnews.com/news/us-news/curfews-may-not-be-enough-keep-peace-tension-builds-coast-n1221531'
    # df = DataFetcher()
    # article = df.fetch(url)
    # print(article.title)
    # print(article.published_date)
    # print(article.authors)
    # print(article.body)
    news = NewsObject(url)
    news.fetch()
    if news.error:
        print(news.error_code)
    else:
        print(news.title)
        print(news.authors)
        print(news.published_date)

    # url = 'https://www.cnn.com/us/live-news/george-floyd-protests-06-02-20/h_b7545fe33352aa03273bb774c926444a'
    # article = Article(url)
    # article.download()
    # article.parse()
    # print(article.title)
    # print(article.authors)
    # print(article.publish_date)
    # print(article.text)