import torch

# Like your "COMPLETE EXAMPLE"
tensor = torch.randn(
    size=(2, 3),
    dtype=torch.float32,
    device='cpu',
    requires_grad=False
)

print(tensor)