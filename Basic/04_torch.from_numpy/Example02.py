import torch
import numpy as np

# 2D numpy array to torch tensor
np_matrix = np.array([[1, 2], [3, 4]])
torch_matrix = torch.from_numpy(np_matrix)

print("NumPy matrix:\n", np_matrix)
print("Torch tensor:\n", torch_matrix)