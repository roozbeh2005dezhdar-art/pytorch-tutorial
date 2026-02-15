import torch

# With no_grad (no gradient tracking)
x = torch.tensor([1.0, 2.0], requires_grad=True)

with torch.no_grad():
    y = x ** 2
    loss = y.sum()
    # No gradient tracking happens here

# loss.backward() would fail here
print("With no_grad - output:", y)
print("No gradients tracked")