import torch

# Basic random tensor
r1 = torch.randn(3)
print(r1)  # tensor([-0.234, 1.567, 0.123])

# 2D random
r2 = torch.randn(2, 3)
print(r2)  # 2x3 with random values