import torch
import numpy as np

# To break memory sharing
np_array = np.array([1, 2, 3])
torch_tensor = torch.from_numpy(np_array).clone()

np_array[0] = 99

print("NumPy array:", np_array)
print("Torch tensor:", torch_tensor)  # Not changed!