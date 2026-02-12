import torch

# Reshape with -1 (infer dimension)
tensor = torch.tensor([1, 2, 3, 4, 5, 6])
reshaped1 = torch.reshape(tensor, (3, -1))  # 3x2
reshaped2 = torch.reshape(tensor, (-1, 2))  # 3x2

print("Original shape:", tensor.shape)
print("Reshape (3, -1):",reshaped1, reshaped1.shape)
print("Reshape (-1, 2):",reshaped2, reshaped2.shape)