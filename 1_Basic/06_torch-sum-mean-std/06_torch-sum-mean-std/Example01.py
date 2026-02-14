import torch

# Sum along a specific dimension
matrix = torch.tensor([[1, 2, 3],
                       [4, 5, 6]])

sum_dim0 = torch.sum(matrix, dim=0)  # Sum columns
sum_dim1 = torch.sum(matrix, dim=1)  # Sum rows

print("Matrix:\n", matrix)
print("Sum along dim=0 (columns):", sum_dim0)
print("Sum along dim=1 (rows):", sum_dim1)