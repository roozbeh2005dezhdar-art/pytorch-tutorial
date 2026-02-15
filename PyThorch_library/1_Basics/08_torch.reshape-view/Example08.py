import torch

# Practical: flatten batch
batch = torch.randn(32, 3, 224, 224)  # Batch of images
flattened = batch.view(32, -1) 

batch2 = torch.randn(32, 3, 224, 224)  # Batch of images
flattened2 = batch2.view(64, -1) 

print("Batch shape:", batch.shape)
print("Flattened shape:", flattened.shape)

print("Batch shape:", batch2.shape)
print("Flattened shape:", flattened2.shape)