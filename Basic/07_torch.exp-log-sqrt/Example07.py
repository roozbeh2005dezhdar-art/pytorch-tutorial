import torch

# Square root matrix
matrix = torch.tensor([[4.0, 9.0],
                       [16.0, 25.0]])
sqrt_matrix = torch.sqrt(matrix)

print("Matrix:\n", matrix)
print("sqrt():\n", sqrt_matrix)