import torch

# Permute vs Transpose (multiple dimensions)
tensor = torch.randn(3, 4, 5)

# Transpose only swaps two dims
t = torch.transpose(tensor, 0, 1)  # (4,3,5)

# Permute can rearrange all dims
p = torch.permute(tensor, (2, 0, 1))  # (5,3,4)

print("Original:", tensor.shape)
print("Transpose (0,1):", t.shape)
print("Permute (2,0,1):", p.shape)