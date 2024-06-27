import torch
from torch import nn
import torchvision
from torchvision import datasets, transforms
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from tqdm.auto import tqdm 
import sys
import os

device = "cuda" if torch.cuda.is_available() else "cpu"