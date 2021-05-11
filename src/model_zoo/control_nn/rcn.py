import torch
from torch import nn


class RecurrentControlNetwork(nn.Module):
    def __init__(self, input_shape, output_shape):
        super().__init__()
        self.linear_part = LinearBlock(input_shape, output_shape)
        self.nonlinear_part = NonLinearBlock(input_shape, 32, output_shape)

    def forward(self, x):
        out_linear = self.linear_part(x)
        out_nonlinear = self.nonlinear_part(x)
        out = torch.clip(torch.add(out_linear, out_nonlinear), -1, 1)
        return out


class LinearBlock(nn.Module):
    def __init__(self, input_shape, output_shape):
        super().__init__()
        self.fc1 = nn.Linear(in_features=input_shape,
                             out_features=output_shape)

    def forward(self, x):
        x = self.fc1(x)
        return x


class NonLinearBlock(nn.Module):
    def __init__(self, input_shape, hidden_size, output_shape):
        super().__init__()
        self.rnn = nn.RNN(input_size=input_shape,
                          hidden_size=32,
                          num_layers=1)
        self.fc1 = nn.Linear(in_features=hidden_size,
                             out_features=output_shape)

    def forward(self, x):
        x = self.rnn(x)
        x = self.fc1(x)
        return x
