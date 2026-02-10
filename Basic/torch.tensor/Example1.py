import torch

# From list
t1 = torch.tensor([1, 2, 3, 4])
print(t1)  # tensor([1, 2, 3, 4])

# 2D from nested list
t2 = torch.tensor([[1, 2], [3, 4]])
print(t2)  # tensor([[1, 2], [3, 4]])

# From tuple
t3 = torch.tensor((5.0, 6.0, 7.0))
print(t3)  # tensor([5., 6., 7.])