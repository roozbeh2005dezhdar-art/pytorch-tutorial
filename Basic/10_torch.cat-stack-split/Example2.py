import torch

# Concatenate 2D tensors along dim=0 (rows)
m1 = torch.tensor([[1, 2],
                   [3, 4]])
m2 = torch.tensor([[5, 6],
                   [7, 8]])
result1 = torch.cat([m1, m2], dim=0)
result2 = torch.cat([m1, m2], dim=1)

print("m1:\n", m1)
print("m2:\n", m2)
print("cat(dim=0):\n", result1)
print("cat(dim=0):\n", result2)