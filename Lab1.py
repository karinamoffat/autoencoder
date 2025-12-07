
import numpy as np
import torch
import torch.nn.functional as F
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import datetime
import argparse

from torchvision.datasets import MNIST
from torch.utils.data import DataLoader

idx = input("Enter an integer between 0 and 59999: ")

train_transform = transforms.Compose([transforms.ToTensor()])
train_set = MNIST('./data/mnist', train=True, transform=train_transform, download=True)

plt.imshow(train_set.data[int (idx)], cmap='gray')
plt.show()