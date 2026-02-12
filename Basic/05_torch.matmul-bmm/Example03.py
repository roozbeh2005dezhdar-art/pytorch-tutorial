import torch

# Matrix-matrix multiplication
A = torch.tensor([[1, 2],
                  [3, 4]])
B = torch.tensor([[5, 6],
                  [7, 8]])
result = torch.matmul(A, B)

print("A:", A)
print("B:", B)
print("A @ B:", result)