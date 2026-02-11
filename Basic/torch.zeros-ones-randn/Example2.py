import torch

# With dtype
z3 = torch.zeros(3, dtype=torch.int64)
print(z3)  # tensor([0, 0, 0], dtype=torch.int64)

# With device
z4 = torch.zeros(3, device='cpu')
print(z4)  # tensor([0., 0., 0.])