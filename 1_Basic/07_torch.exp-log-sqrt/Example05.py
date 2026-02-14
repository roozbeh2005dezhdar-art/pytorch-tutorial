import torch

# Log base 2
tensor = torch.tensor([1.0, 2.0, 4.0, 8.0])
log2_tensor = torch.log2(tensor)

print("Input:", tensor)
print("log2():", log2_tensor)  # log2(1)=0, log2(2)=1, log2(4)=2, log2(8)=3