import torch

# Like your "PRACTICAL TRAINING DATA" example
X = torch.randn(100, 10, dtype=torch.float32)  # 100 samples, 10 features
y = torch.zeros(100, dtype=torch.int64)        # 100 labels

print(f"X shape: {X.shape}, dtype: {X.dtype}")
print(f"y shape: {y.shape}, dtype: {y.dtype}")