import torch

# Exponential (e^x)
tensor = torch.tensor([0.0, 1.0, 2.0])
exp_tensor = torch.exp(tensor)

print("Input:", tensor)
print("exp():", exp_tensor)  # e^0=1, e^1≈2.718, e^2≈7.389