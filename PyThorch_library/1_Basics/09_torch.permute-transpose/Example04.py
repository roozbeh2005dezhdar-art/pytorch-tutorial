import torch

# Transpose specific dimensions
tensor = torch.randn(2, 3, 4)
transposed_0_2 = torch.transpose(tensor, 0, 2)  # Swap dim0 and dim2

print("Original shape:", tensor.shape)
print("Transpose(0,2) shape:", transposed_0_2.shape)  # (4,3,2)