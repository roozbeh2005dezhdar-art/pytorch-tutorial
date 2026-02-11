import torch

# PyTorch guesses the type
a = torch.tensor([1, 2])        # → torch.int64
b = torch.tensor([1.0, 2.0])    # → torch.float32  
c = torch.tensor([True, False]) # → torch.bool

print(a)
print(b)
print(c)