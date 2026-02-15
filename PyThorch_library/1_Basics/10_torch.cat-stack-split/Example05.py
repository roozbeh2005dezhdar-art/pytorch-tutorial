import torch

# Stack 2D tensors
m1 = torch.tensor([[1, 2],
                   [3, 4]])
m2 = torch.tensor([[5, 6],
                   [7, 8]])

stacked = torch.stack([m1, m2], dim=0)

print("m1 shape:", m1.shape)
print("m2 shape:", m2.shape)
print("stacked shape:", stacked.shape)  # (2, 2, 2)
print("stacked:\n", stacked)