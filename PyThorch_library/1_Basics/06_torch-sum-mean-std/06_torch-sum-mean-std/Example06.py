import torch

# Standard deviation along dimension
matrix = torch.tensor([[1.0, 2.0, 3.0],
                       [4.0, 5.0, 6.0]])

std_dim0 = torch.std(matrix, dim=0)  # Std of columns
std_dim1 = torch.std(matrix, dim=1)  # Std of rows

print("Matrix:\n", matrix)
print("Std along dim=0:", std_dim0)
print("Std along dim=1:", std_dim1)