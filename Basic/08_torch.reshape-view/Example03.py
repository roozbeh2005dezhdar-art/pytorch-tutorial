import torch

# Reshape 2D to 1D
matrix = torch.tensor([[1, 2, 3],
                       [4, 5, 6]])
flat = torch.reshape(matrix, (-1,))

print("Matrix:\n", matrix, matrix.shape)
print("Flattened:", flat, flat.shape)