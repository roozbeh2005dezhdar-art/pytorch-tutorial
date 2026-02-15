import torch

# Practical: batch concatenation
batch1 = torch.randn(16, 3, 32, 32)  # 16 images
batch2 = torch.randn(24, 3, 32, 32)  # 24 images
full_batch = torch.cat([batch1, batch2], dim=0)

print("batch1 shape:", batch1.shape)
print("batch2 shape:", batch2.shape)
print("full_batch shape:", full_batch.shape)  # 40, 3, 32, 32