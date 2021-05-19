import torch
from torch import nn
from .linear import LinearBlock
from .mlp import MultiLayerPerceptron as NonLinearBlock


class StructuredControlNetwork(nn.Module):
    def __init__(self, input_shape, output_shape):
        super().__init__()
        self.linear_part = LinearBlock(input_shape, output_shape)
        self.nonlinear_part = NonLinearBlock(input_shape, 32, output_shape)

    def forward(self, x):
        out_linear = self.linear_part(x)
        out_nonlinear = self.nonlinear_part(x)
        out = torch.clip(torch.add(out_linear, out_nonlinear), -1, 1)
        return out
