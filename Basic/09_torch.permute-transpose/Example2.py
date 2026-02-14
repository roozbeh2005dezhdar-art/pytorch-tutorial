import torch

# Multiple permutations
tensor = torch.randn(2, 3, 5, 7)
p1 = torch.permute(tensor, (2, 0, 3, 1))
p2 = torch.permute(tensor, (3, 2, 1, 0))

print("Original shape:", tensor.shape)
print("Permuted 1 shape:", p1.shape)
print("Permuted 2 shape:", p2.shape)