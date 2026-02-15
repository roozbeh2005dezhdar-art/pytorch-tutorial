import torch

# View (similar to reshape)
tensor = torch.tensor([1, 2, 3, 4, 5, 6])
viewed = tensor.view(2, 3)

print("Original:", tensor, tensor.shape)
print("Viewed (2,3):\n", viewed, viewed.shape)