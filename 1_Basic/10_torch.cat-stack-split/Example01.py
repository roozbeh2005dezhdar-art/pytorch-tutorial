import torch

# Concatenate 1D tensors
t1 = torch.tensor([1, 2, 3])
t2 = torch.tensor([4, 5, 6])
result = torch.cat([t1, t2])

print("t1:", t1)
print("t2:", t2)
print("cat():", result)  # [1, 2, 3, 4, 5, 6]