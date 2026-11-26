
import torch

# Shuffle Tensors
def shuffle():
  x = torch.tensor([[10, 11], [20, 21], [30, 31], [40, 41]])
  idx = torch.randperm(x.size(0))
  return = x[idx]
