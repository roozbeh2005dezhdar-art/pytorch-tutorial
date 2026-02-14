import torch

# Save a tensor
tensor = torch.tensor([1, 2, 3, 4])
torch.save(tensor, 'my_tensor.pt')
print("Tensor saved to 'my_tensor.pt'")
print("Saved tensor:", tensor)