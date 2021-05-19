from torch import nn


class LinearBlock(nn.Module):
    def __init__(self, input_shape, output_shape):
        super().__init__()
        self.fc1 = nn.Linear(in_features=input_shape,
                             out_features=output_shape)

    def forward(self, x):
        x = self.fc1(x)
        return x
