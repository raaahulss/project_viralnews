# pesudo model functions
def viralness_model(news):
    return 0.5


def sentiment_model(news):
    return 0.5


def public_opinion_model(twitter):
    return 0.5


class Aggregator(object):
    def __init__(self, news=None, twitter=None, published=False):
        self.news = news
        self.twitter = twitter
        self.published = published
        self.models = {'viralness': None,
                       'sentiment': None,
                       'public_opinion': None}
        self.error = False
        self.error_code = ''

    def run_models(self):
        if not self.news:
            self.error = True
            self.error_code = 'none_news_object'
            return

        self.models['viralness'] = viralness_model(self.news)
        self.models['sentiment'] = sentiment_model(self.news)
        if self.published:
            self.models['public_opinion'] = public_opinion_model(self.twitter)


if __name__ == '__main__':
    agg = Aggregator(1, 1, True)
    agg.run_models()
    print(agg.models)