

import torch
import torch.nn.functional as F
import torch.nn as nn
from torchsummary import summary

print(summary)

class autoencoderMLP4Layer(nn.Module):

	def __init__(self, N_input=784, N_bottleneck=8, N_output=784):
		super (autoencoderMLP4Layer, self).__init__()

	def forward(self, X):
		return X




