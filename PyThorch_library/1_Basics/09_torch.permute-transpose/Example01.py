import torch

# Image channels reordering (C, H, W) -> (H, W, C)
image_cwh = torch.randn(3, 224, 224)  # Channels first
image_whc = torch.permute(image_cwh, (1, 2, 0))  # Channels last

print("Channels first:", image_cwh.shape)
print("Channels last:", image_whc.shape)