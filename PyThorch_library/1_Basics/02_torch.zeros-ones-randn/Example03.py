import torch

# With requires_grad
z5 = torch.zeros(3, requires_grad=True)
print(z5)  # tensor([0., 0., 0.], requires_grad=True)

# Complete
z6 = torch.zeros(2, 3, dtype=torch.float32, device='cpu', requires_grad=False)
print(z6)