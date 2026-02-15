import torch

# With dtype
r3 = torch.randn(3, dtype=torch.float64)
print(r3.dtype)  # torch.float64

# With device
r4 = torch.randn(3, device='cpu')
print(r4)