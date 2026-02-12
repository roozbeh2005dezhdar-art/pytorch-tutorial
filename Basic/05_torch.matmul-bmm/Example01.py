import torch

# Vector-vector multiplication
v1 = torch.tensor([1, 2, 3])
v2 = torch.tensor([4, 5, 6])
result = torch.matmul(v1, v2)

print("Vector dot product:", result)
print("Same as:", torch.sum(v1 * v2)) # v1 * v2 = (1×4) + (2×5) + (3×6) = 4 + 10 + 18 = 32