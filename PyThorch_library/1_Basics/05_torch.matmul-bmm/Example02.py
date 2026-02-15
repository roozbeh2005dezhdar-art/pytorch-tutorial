import torch

# Matrix-vector multiplication
M = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])
v = torch.tensor([1, 0, 2])
result = torch.matmul(M, v)

print("Matrix:", M)
print("Vector:", v)
print("Result:", result)