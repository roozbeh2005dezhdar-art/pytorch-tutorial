import torch
import numpy as np

# Shared memory (changes affect both)
np_array = np.array([1, 2, 3])
torch_tensor = torch.from_numpy(np_array)

np_array[0] = 99  # Change in NumPy

print("NumPy array:", np_array)
print("Torch tensor:", torch_tensor)  # Also changed!