import torch

# Combined: RMS (Root Mean Square)
values = torch.tensor([1.0, 2.0, 3.0, 4.0])
rms = torch.sqrt(torch.mean(values ** 2))

print("Values:", values)
print("RMS:", rms)