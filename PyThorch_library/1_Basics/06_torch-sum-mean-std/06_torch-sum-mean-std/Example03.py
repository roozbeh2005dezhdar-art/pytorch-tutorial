import torch

# Mean along specific dimension
matrix = torch.tensor([[1.0, 2.0, 3.0],
                       [4.0, 5.0, 6.0]])

mean_dim0 = torch.mean(matrix, dim=0)  # Mean of columns
mean_dim1 = torch.mean(matrix, dim=1)  # Mean of rows

print("Matrix:\n", matrix)
print("Mean along dim=0:", mean_dim0)
print("Mean along dim=1:", mean_dim1)