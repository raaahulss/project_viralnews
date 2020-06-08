from torch import nn


class SentimentModel(nn.Module):
    def __init__(self):
        super(SentimentModel, self).__init__()

    def forward(self, news):
        return 0.5
