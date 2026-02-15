import torch

# Load a saved tensor
loaded_tensor = torch.load('my_tensor.pt')
print("Loaded tensor:", loaded_tensor)
print("Loaded dtype:", loaded_tensor.dtype)