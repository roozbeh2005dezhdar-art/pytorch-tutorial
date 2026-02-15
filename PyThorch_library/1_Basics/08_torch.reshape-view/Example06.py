import torch

# View with -1
tensor = torch.tensor([1, 2, 3, 4, 5, 6])
viewed1 = tensor.view(3, -1)
viewed2 = tensor.view(-1, 2)

print("View (3, -1):",viewed1, viewed1.shape)
print("View (-1, 2):",viewed2, viewed2.shape)