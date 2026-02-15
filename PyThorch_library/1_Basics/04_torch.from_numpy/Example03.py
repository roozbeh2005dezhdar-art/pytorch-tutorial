import torch
import numpy as np

# With different dtypes
np_float = np.array([1.0, 2.0, 3.0], dtype=np.float32)
torch_float = torch.from_numpy(np_float)

print("NumPy float32:", np_float.dtype)
print("Torch tensor dtype:", torch_float.dtype)