import torch

# Complete example
l6 = torch.linspace(
    start=0,
    end=1,
    steps=10,
    dtype=torch.float32,
    device='cpu',
    requires_grad=False
)
print("Complete linspace:", l6)
# 10 evenly spaced values from 0 to 1