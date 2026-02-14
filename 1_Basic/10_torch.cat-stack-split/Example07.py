import torch

# Split 2D tensor along dim=0 (rows)
matrix = torch.tensor([[1, 1],
                       [2, 2],
                       [3, 3],
                       [4, 4],
                       [5, 5]])
splits = torch.split(matrix, 2, dim=0)  # Split into chunks of 2 rows


print(splits)