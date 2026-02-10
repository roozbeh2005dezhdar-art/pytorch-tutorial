import torch

# CPU (always works)
cpu_tensor = torch.tensor([1, 2], device='cpu')
print(cpu_tensor)

# GPU (only if available)
if torch.cuda.is_available():
    gpu_tensor = torch.tensor([1, 2], device='cuda')
    print(gpu_tensor)