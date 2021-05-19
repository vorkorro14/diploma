from torch import nn


class RecurrentBlock(nn.Module):
    def __init__(self, input_shape, hidden_size, output_shape):
        super().__init__()
        self.rnn = nn.RNN(input_size=input_shape,
                          hidden_size=32,
                          num_layers=1)
        self.fc = nn.Linear(in_features=hidden_size,
                            out_features=output_shape)

    def forward(self, x):
        x = self.rnn(x)
        x = self.fc(x)
        return x
