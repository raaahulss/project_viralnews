import pickle
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from keras import Model
from src.collection.twitter_api import Tweet


def load_tokenizer_and_model() -> [Tokenizer, Model]:
    """
    Load model and tokenizer from file
    :return:
    """
    with open('./src/models/public_opinion.vocab', 'rb') as f:
        tokenizer = pickle.load(f)
    model = load_model('./src/models/public_opinion.model')
    return tokenizer, model


def get_public_opinion(tweet: Tweet) -> float:
    tokenizer, model = load_tokenizer_and_model()
    seq_test = tokenizer.texts_to_sequences(tweet.responses)
    padded_seq_test = pad_sequences(seq_test, maxlen=45)
    yhat_cnn = model.predict(padded_seq_test)
    return float(yhat_cnn.mean())
