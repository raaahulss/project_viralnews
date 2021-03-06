import boto3
from io import BytesIO
import json
import torch
from torch import nn

from src.collection.news_fetcher import NewsObject


class SentimentModel(nn.Module):
    def __init__(self, vocab: dict, output_size: int):
        super(SentimentModel, self).__init__()
        self.vocab = vocab
        self.input_size = len(vocab)
        self.output_size = output_size
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.linear = nn.Linear(self.input_size, self.output_size).to(self.device)

    def forward(self, sentence: str) -> float:
        bow_vec = self.make_bow_vec(sentence)
        return nn.functional.softmax(self.linear(bow_vec), dim=-1)[0][0].item()

    def make_bow_vec(self, sentence: str) -> torch.Tensor:
        bow_vec = torch.zeros(len(self.vocab), device=self.device)
        for word in sentence.lower().split():
            if word in self.vocab:
                bow_vec[self.vocab[word]] += 1
        return bow_vec.view(1, -1)


def load_vocab_and_model():
    s3 = boto3.resource('s3')
    vocab = json.load(
        BytesIO(s3.Object('project-viralnews-model', 'sentiment_analysis.vocab').get()['Body'].read())
    )
    model = SentimentModel(vocab, 2)
    model.load_state_dict(torch.load(
        BytesIO(s3.Object('project-viralnews-model', 'sentiment_analysis.model').get()['Body'].read()),
        map_location=model.device
    ))
    return vocab, model


def get_sentiment(news: NewsObject) -> float:
    """
    Given a news object, return the probability that its underlying sentiment is liberal
    """
    return sentiment_model(news.title + news.content)


# only load once when the server starts
sentiment_vocab, sentiment_model = load_vocab_and_model()
