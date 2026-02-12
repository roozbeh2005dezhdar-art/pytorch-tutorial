import torch

# Reshape 1D to 2D
tensor = torch.tensor([1, 2, 3, 4, 5, 6])
reshaped = torch.reshape(tensor, (2, 3))

print("Original:", tensor, tensor.shape)
print("Reshaped (2,3):\n", reshaped, reshaped.shape)