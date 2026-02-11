import torch

source = torch.tensor([1.0, 2.0], dtype=torch.float64)
new = torch.tensor(source)  # Inherits float64
print(new.dtype)  # torch.float64
print(new)