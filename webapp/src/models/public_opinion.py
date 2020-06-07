from torch import nn


class PublicOpinionModel(nn.Module):
    def __init__(self):
        super(PublicOpinionModel, self).__init__()

    def forward(self, twitter):
        return 0.5
