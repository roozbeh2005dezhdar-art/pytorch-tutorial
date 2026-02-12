import torch

# Reshape 3D to 2D
tensor_3d = torch.randn(2, 3, 4)  # 2x3x4
tensor_2d = torch.reshape(tensor_3d, (6, 4))  # 6x4

print("3D shape:", tensor_3d, tensor_3d.shape)
print("Reshaped 2D shape:", tensor_2d, tensor_2d.shape)