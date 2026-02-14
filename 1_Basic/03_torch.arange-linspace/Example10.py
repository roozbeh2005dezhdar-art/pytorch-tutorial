import torch

# With requires_grad
l5 = torch.linspace(0, 2, 3, requires_grad=True)
print("linspace with requires_grad:", l5)
# tensor([0., 1., 2.], requires_grad=True)