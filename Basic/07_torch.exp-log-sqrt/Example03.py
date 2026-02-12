import torch

# Natural log (ln)
tensor = torch.tensor([1.0, 2.7183, 10.0])
log_tensor = torch.log(tensor)

print("Input:", tensor)
print("log():", log_tensor)  # ln(1)=0, ln(e)≈1, ln(10)≈2.3