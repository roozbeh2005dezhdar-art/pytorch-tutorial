import torch

# Features (X) and labels (y) for ML
X = torch.tensor([[0.1, 0.2], [0.3, 0.4]], dtype=torch.float32)
y = torch.tensor([0, 1], dtype=torch.int64)

print(f"X shape: {X.shape}, dtype: {X.dtype}")
print(f"y shape: {y.shape}, dtype: {y.dtype}")