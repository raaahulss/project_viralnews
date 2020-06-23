from src.models.viralness import get_viralness
from src.models.sentiment import get_sentiment
from src.models.public_opinion import get_public_opinion
from src.collection.news_fetcher import NewsObject


class Aggregator(object):
    def __init__(self, news: NewsObject = None, twitter=None, published: bool = False):
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
    agg = Aggregator(1, 1, True)
    agg.run_models()
    print(agg.models)
