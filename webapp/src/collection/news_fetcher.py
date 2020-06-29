from docx import Document
from newspaper import Article, ArticleException
from datetime import datetime
from src.error import ApplicationError, error_list


# class DataFetcher(object):
#     """Fetch data from supported domains
#     Attributes:
#         supported_domains: A list of supported domains.
#     """
#     def __init__(self, supported_sources=('twitter', 'nytimes', 'washingtonpost')):
#         self.supported_sources = supported_sources
#
#     def parse_url(self, url):
#         """Parse a given url to determine whether it is a valid url and whether the source is supported.
#         Args:
#             url: A url given by user.
#         Returns:
#             Return error code if the source is not supported or invalid. Return the source otherwise.
#         """
#         if not validators.url(url):
#             print('invalid url')
#             return -1
#
#         _, source, _ = tldextract.extract(url)
#         if tldextract.extract(url).domain in self.supported_sources:
#             return source
#         else:
#             print('unsupported source')
#             return -1   # Error codes are not defined yet, use -1 for convenience
#
#     def fetch_news(self, url, source):
#         """Extract info from a news article.
#         Arguments:
#             url: url of the news article
#             source: Source of the news article.
#         Returns:
#             Return an object of the extracted news article, or status code if there is an error.
#         """
#         article = NewsObject.factory(source)
#         article.get(url)
#         return article
#
#     def fetch_twitter(self, url):
#         # TODO
#         raise NotImplementedError
#
#     def fetch(self, url):
#         source = self.parse_url(url)
#         if source == -1:
#             return -1
#         elif source == 'twitter':
#             print('fetch twitter')
#             return self.fetch_twitter(url)
#         else:
#             article = self.fetch_news(url, source)
#             if article.status_code == 200:
#                 return article
#             else:
#                 return article.status_code
#
#
# class NewsObject(object):
#     """News article base class
#     """
#     def __init__(self):
#         self.status_code = None
#         self.title = None
#         self.content = None
#         self.date = None
#
#     @staticmethod
#     def factory(source):
#         """Create new object based on subclass type
#         Arguments:
#             source: Source of the news article
#         Returns:
#             Return the
#         """
#         if source == 'nytimes':
#             return NyTimes()
#         elif source == 'washingtonpost':
#             return WashingtonPost()
#         else:
#             print('unsupported source')
#             exit(-1)
#
#
# class NyTimes(NewsObject):
#     def get(self, url):
#         r = requests.get(url)
#         tree = html.fromstring(r.content)
#         self.status_code = r.status_code
#         self.title = tree.xpath('//title/text()')[0]
#         self.content = ' '.join([element.text_content()
#                                  for element in tree.xpath('//div[contains(@class,"StoryBodyCompanionColumn")]/div/p')])
#         self.date = tree.xpath('//meta[@property="article:published"]/@content')[0]
#
#
# class WashingtonPost(NewsObject):
#     def get(self, url):
#         r = requests.get(url)
#         tree = html.fromstring(r.content)
#         self.status_code = r.status_code
#         self.title = tree.xpath('//title/text()')[0]
#         self.content = ' '.join([element.text_content()
#                                  for element in tree.xpath('//div[@class="article-body"]/div/section/div')])
#         self.date = tree.xpath('//meta[@name="last_updated_date"]/@content')[0]


class NewsObject(object):
    def __init__(self, url):
        self.url = url
        self.title = ''
        self.published_date = ''
        self.authors = ''
        self.content = ''
        self.error = False
        self.error_code = ''

    def fetch_from_url(self):
        """
        Given a news article url, fetch its metadata and content.
        """
        article = Article(self.url)
        try:
            article.download()
            article.parse()
            self.title = article.title
            self.published_date = article.publish_date
            self.authors = article.authors
            self.content = article.text
        except ArticleException:
            self.error = True
            self.error_code = "connection_error"

    def fetch_from_file(self):
        """
        Parse a file to extract its title and body
        :param file_path: path of a file
        :return: title and body of the file
        """
        doc = Document(self.url)
        content = []
        for paragraph in doc.paragraphs:
            if not self.title:
                self.title = paragraph.text
            else:
                content.append(paragraph.text)
        self.content = ' '.join(content)
        self.url = ''

    def to_dict(self) -> dict:
        """
        Transform this news object to a dict.
        :return: A dict of related member variables.
        """
        return {'metadata': {'error': self.error,
                             'error_code': self.error_code},
                'details': {'title': self.title,
                            'authors': self.authors,
                            'published_date': self.published_date,
                            'content': self.content,
                            'url': self.url}}


def get_news_from_file(path: str) -> [NewsObject, ApplicationError]:
    try:
        word_file = NewsObject(path)
        word_file.fetch_from_file()
        if word_file.error:
            raise ApplicationError(*error_list["UNBL_FTCH_NEWS"])
        return word_file, None
    except ApplicationError as err:
        return None, err


def get_news_from_url(url: str) -> [NewsObject, ApplicationError]:
    try:
        news = NewsObject(url)
        news.fetch_from_url()
        # expecting that in case of error you throw error
        if news.error:
            raise ApplicationError(*error_list["UNBL_FTCH_NEWS"])
        return news, None
    except ApplicationError as err:
        return None, err
