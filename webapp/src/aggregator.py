from src.models.viralness import get_viralness
from src.models.sentiment import get_sentiment
from src.models.public_opinion import get_public_opinion
from src.collection.news_fetcher import NewsObject
from src.collection.twitter_api import Tweet
from src.error import *


class Aggregator(object):
    def __init__(self, news: NewsObject = None, tweet: Tweet = None, is_twitter: bool = False):
        self.news = news
        self.tweet = tweet
        self.is_twitter = is_twitter
        self.models = {'viralness': None,
                       'sentiment': None,
                       'public_opinion': None}
        self.error = None

    def run_models(self):
        """
        Run the given article via sentiment analysis model. If the article is published, run it via viralness model and
        public opinion model too.
        """
        if not self.news:
            raise ApplicationError(*error_list["FILE_NT_FND"])

        self.models['sentiment'] = get_sentiment(self.news)
        # we might use virality model based on text for virality
        self.models['viralness'] = get_viralness(self.news)
        if self.is_twitter:
            self.models['public_opinion'] = get_public_opinion(self.tweet)

    def to_dict(self):
        dictionary = {"viralness" : self.models['viralness'],
                       "sentiment" : self.models['sentiment'] }
        if self.is_twitter:
            dictionary["public_opinion"] = self.models['public_opinion']
        return dictionary


if __name__ == '__main__':
    news = NewsObject('')
    news.title = 'test'
    news.content = 'test'
    tweet = ['awww that bummer you shoulda got david carr of third day to do it',
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
    agg = Aggregator(news, tweet, True)
    agg.run_models()
    print(agg.models)
