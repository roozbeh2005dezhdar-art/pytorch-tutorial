import torch

# Learning rate schedule
learning_rates = torch.linspace(0.01, 0.001, 100)
print("Learning rates:", learning_rates[:5])
# Gradually decreasing learning rates