
import torch

# Shuffle Tensors
def shuffle(tens):
  idx = torch.randperm(tens.size(0))
  return x[idx]
