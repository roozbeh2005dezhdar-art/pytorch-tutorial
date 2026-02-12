import torch

# Normalization: (x - mean) / std
data = torch.randn(100)  # 100 random samples

mean_val = torch.mean(data)
std_val = torch.std(data)
normalized = (data - mean_val) / std_val

print("Original mean/std:", mean_val.item(), std_val.item())
print("Normalized mean/std:", 
      torch.mean(normalized).item(), 
      torch.std(normalized).item())