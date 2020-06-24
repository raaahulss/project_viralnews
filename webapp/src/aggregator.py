from src.models.viralness import get_viralness
from src.models.sentiment import get_sentiment
from src.models.public_opinion import get_public_opinion
from src.collection.news_fetcher import NewsObject
from src.collection.twitter_api import Tweet


class Aggregator(object):
    def __init__(self, news: NewsObject = None, twitter : Tweet=None, published: bool = False):
        self.news = news
        self.twitter = twitter
        self.published = published
        self.models = {'viralness': None,
                       'sentiment': None,
                       'public_opinion': None}
        self.error = False
        self.error_code = ''

    def run_models(self):
        """
        Run the given article via sentiment analysis model. If the article is published, run it via viralness model and
        public opinion model too.
        """
        if not self.news:
            self.error = True
            self.error_code = 'none_news_object'
            return

        self.models['sentiment'] = get_sentiment(self.news)
        if self.published:
            self.models['viralness'] = get_viralness(self.news)
            self.models['public_opinion'] = get_public_opinion(self.twitter)


if __name__ == '__main__':
    news = NewsObject('')
    news.title = 'test'
    news.content = 'test'
    twitter = ['awww that bummer you shoulda got david carr of third day to do it',
               'is upset that he can not update his facebook by texting it and might cry as result school today also blah',
               'dived many times for the ball managed to save the rest go out of bounds',
               'my whole body feels itchy and like its on fire',
               'no it not behaving at all mad why am here because can not see you all over there',
               'not the whole crew',
               'need hug',
               'hey long time no see yes rains bit only bit lol fine thanks how you',
               'nope they did not have it',
               'que me muera',
               'love guys the best',
               'im meeting up with one of my besties tonight cant wait girl talk',
               'thanks for the twitter add sunisa got to meet you once at hin show here in the dc area and you were sweetheart',
               'being sick can be really cheap when it hurts too much to eat real food plus your friends make you soup',
               'he has that effect on everyone',
               'you can tell him that just burst out laughing really loud because of that thanks for making me come out of my sulk',
               'thans for your response ihad already find this answer',
               'am so jealous hope you had great time in vegas how did you like the acm love your show',
               'ah congrats mr fletcher for finally joining twitter',
               'responded stupid cat is helping me type forgive errors']
    agg = Aggregator(news, twitter, True)
    agg.run_models()
    print(agg.models)
