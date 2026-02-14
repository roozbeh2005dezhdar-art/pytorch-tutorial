import torch

# With dtype parameter
l4 = torch.linspace(0, 1, 5, dtype=torch.float64)
print("linspace with float64:", l4)
# tensor([0.0000, 0.2500, 0.5000, 0.7500, 1.0000], dtype=torch.float64)