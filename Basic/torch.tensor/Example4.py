import torch

# For training (tracks gradients)
trainable = torch.tensor([1.0, 2.0], requires_grad=True)
print(trainable)

# For data (no gradient needed)
data_only = torch.tensor([1.0, 2.0], requires_grad=False)
print(data_only)