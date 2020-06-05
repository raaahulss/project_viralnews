from torch import nn


# pesudo model functions
class ViralnessModel(nn.Module):
    def __init__(self):
        super(ViralnessModel, self).__init__()

    def forward(self, news):
        return 0.5


class SentimentModel(nn.Module):
    def __init__(self):
        super(SentimentModel, self).__init__()

    def forward(self, news):
        return 0.5


class PublicOpinionModel(nn.Module):
    def __init__(self):
        super(PublicOpinionModel, self).__init__()

    def forward(self, twitter):
        return 0.5
