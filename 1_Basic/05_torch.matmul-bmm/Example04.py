import torch

# Batch matrix multiplication
batch_A = torch.randn(3, 4, 5)  # 3 batches of 4x5 matrices
print(batch_A)
batch_B = torch.randn(3, 5, 6)  # 3 batches of 5x6 matrices
result = torch.matmul(batch_A, batch_B)

print("batch_A shape:", batch_A.shape)
print("batch_B shape:", batch_B.shape)
print("Result shape:", result.shape)  # 3x4x6