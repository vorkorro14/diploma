import torch
from torch import nn


class MultiLayerPerceptron(nn.Module):
    def __init__(self, input_shape, hidden_size, output_shape):
        super().__init__()
        # self.rnn = nn.RNN(input_size=input_shape,
        #                   hidden_size=32,
        #                   num_layers=1)
        self.fc1 = nn.Linear(in_features=input_shape,
                             out_features=hidden_size)
        self.fc2 = nn.Linear(in_features=hidden_size,
                             out_features=hidden_size)
        self.fc3 = nn.Linear(in_features=hidden_size,
                             out_features=output_shape)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        # x = self.fc1(x)
        # x = self.fc2(x)
        # x = self.fc3(x)
        return x
