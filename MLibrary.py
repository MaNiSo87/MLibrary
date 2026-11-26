import matplotlib.pyplot as plt
import torch

# Shuffle Tensors
def shuffle(tens):
  idx = torch.randperm(tens.size(0))
  return tens[idx]

# Plot Train, Test and Preditction data
def plot_data(train_data, train_labels, test_data, test_labels, predictions=None):
    plt.figure(figsize=(10, 7))

    plt.scatter(train_data, train_labels, c="b", s=4, label="Training data")

    plt.scatter(test_data, test_labels, c="g", s=4, label="Testing data")

    if predictions is not None:
      plt.scatter(test_data, predictions, c="r", s=4, label="Predictions")

    plt.legend(prop={"size": 14});
