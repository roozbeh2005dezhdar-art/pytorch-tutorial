import torch

# Keep dimensions
matrix = torch.tensor([[1, 2, 3],
                       [4, 5, 6]])

sum_keep = torch.sum(matrix, dim=1, keepdim=True)

print("Matrix:\n", matrix)
print("Sum with keepdim=True:\n", sum_keep)
print("Shape:", sum_keep.shape)