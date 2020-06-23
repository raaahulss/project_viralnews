from torch import nn


class PublicOpinionModel(nn.Module):
    def __init__(self):
        super(PublicOpinionModel, self).__init__()

    def forward(self, twitter) -> float:
        return 0.5


def get_public_opinion(twitter) -> float:
    public_opinion_model = PublicOpinionModel()
    return public_opinion_model(twitter)
