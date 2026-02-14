import torch

# Transpose 2D matrix
matrix = torch.tensor([[1, 2, 3],
                       [4, 5, 6]])
transposed = torch.transpose(matrix, 0, 1)  # Swap rows and columns

print("Matrix:\n", matrix)
print("Transposed:\n", transposed)