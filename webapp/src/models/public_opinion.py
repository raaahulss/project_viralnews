import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from keras import Model


def load_tokenizer_and_model() -> [Tokenizer, Model]:
    """
    Load model and tokenizer from file
    :return:
    """
    csv = '/Users/xie/Documents/cmu/capstone/project_viralnews/webapp/src/models/clean_tweet_1.csv'
    my_df = pd.read_csv(csv, index_col=0)
    my_df.head()
    my_df.dropna(inplace=True)
    my_df.reset_index(drop=True, inplace=True)
    my_df.info()
    x = my_df.text
    tokenizer = Tokenizer(num_words=100000)
    tokenizer.fit_on_texts(x)
    model = load_model('/Users/xie/Documents/cmu/capstone/project_viralnews/webapp/src/models/CNN_best_weights.02-0.8318.hdf5')
    return tokenizer, model


def get_public_opinion(twitter: [str]) -> float:
    tokenizer, model = load_tokenizer_and_model()
    seq_test = tokenizer.texts_to_sequences(twitter)
    padded_seq_test = pad_sequences(seq_test, maxlen=45)
    yhat_cnn = model.predict(padded_seq_test)
    return yhat_cnn.mean()


if __name__ == '__main__':
    test = ['awww that bummer you shoulda got david carr of third day to do it',
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
    print(get_public_opinion(test))
