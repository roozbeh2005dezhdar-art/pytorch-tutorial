import torch

# With dtype parameter
a5 = torch.arange(3, dtype=torch.float32)
print("arange(3, dtype=float32):", a5)
# tensor([0., 1., 2.])