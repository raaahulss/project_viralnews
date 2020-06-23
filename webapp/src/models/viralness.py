from torch import nn

from src.collection.news_fetcher import NewsObject


# pesudo model functions
class ViralnessModel(nn.Module):
    def __init__(self):
        super(ViralnessModel, self).__init__()

    def forward(self, news):
        return 0.5


def get_viralness(news: NewsObject) -> float:
    viralness_model = ViralnessModel()
    return viralness_model(news)
