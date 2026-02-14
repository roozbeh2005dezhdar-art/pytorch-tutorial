import torch

# Split with different chunk sizes
tensor = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
splits = torch.split(tensor, [3, 2, 5])  # Custom sizes

print(splits)    