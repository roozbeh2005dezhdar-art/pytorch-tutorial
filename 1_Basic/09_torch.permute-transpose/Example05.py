import torch

# .T shortcut for 2D transpose
matrix = torch.tensor([[1, 2],
                       [3, 4],
                       [5, 6]])

print("Original shape:", matrix.shape)
print(".T shape:", matrix.T.shape)
print(".T:\n", matrix.T)