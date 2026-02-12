import torch

# Log base 10
tensor = torch.tensor([1.0, 10.0, 100.0])
log10_tensor = torch.log10(tensor)

print("Input:", tensor)
print("log10():", log10_tensor)  # log10(1)=0, log10(10)=1, log10(100)=2