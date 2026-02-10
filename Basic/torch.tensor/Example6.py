import torch

original = [1, 2, 3]
tensor = torch.tensor(original)  # Makes a copy
original[0] = 999  # Doesn't affect tensor
print(tensor)  # Still [1, 2, 3]
print(original)