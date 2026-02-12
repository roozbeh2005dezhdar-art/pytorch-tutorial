import torch

# With dtype
o3 = torch.ones(3, dtype=torch.int32)
print(o3)  # tensor([1, 1, 1], dtype=torch.int32)

# Bool ones
o4 = torch.ones(3, dtype=torch.bool)
print(o4)  # tensor([True, True, True])