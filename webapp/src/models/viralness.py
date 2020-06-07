from torch import nn


# pesudo model functions
class ViralnessModel(nn.Module):
    def __init__(self):
        super(ViralnessModel, self).__init__()

    def forward(self, news):
        return 0.5
