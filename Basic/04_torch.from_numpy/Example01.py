import torch
import numpy as np

# Convert numpy array to torch tensor
np_array = np.array([1, 2, 3, 4])
tensor = torch.from_numpy(np_array)

print("NumPy array:", np_array)
print("Torch tensor:", tensor)
print("Type:", type(tensor))