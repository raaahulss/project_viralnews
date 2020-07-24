import boto3
from io import BytesIO
import h5py
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
    s3 = boto3.resource('s3')
    tokenizer = pickle.load(
        BytesIO(s3.Object('project-viralnews-model', 'public_opinion.vocab').get()['Body'].read())
    )
    model = load_model(
        h5py.File(BytesIO(s3.Object('project-viralnews-model', 'public_opinion.model').get()['Body'].read()))
    )
    return tokenizer, model


def get_public_opinion(tweet: Tweet) -> float:
    seq_test = public_opinion_tokenizer.texts_to_sequences(tweet.responses)
    padded_seq_test = pad_sequences(seq_test, maxlen=45)
    yhat_cnn = public_opinion_model.predict(padded_seq_test)
    return float(yhat_cnn.mean())


# only load once when the server starts
public_opinion_tokenizer, public_opinion_model = load_tokenizer_and_model()
