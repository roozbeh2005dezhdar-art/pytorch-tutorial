import torch

# Concatenate multiple tensors
t1 = torch.tensor([1, 2])
t2 = torch.tensor([3, 4])
t3 = torch.tensor([5, 6])
t4 = torch.tensor([7, 8])

result = torch.cat([t1, t2, t3, t4])
print("Multiple cat():", result)  # [1, 2, 3, 4, 5, 6, 7, 8]