import torch

# Float 32 (standard for ML)
float_tensor = torch.tensor([1.5, 2.7], dtype=torch.float32)
print(float_tensor)

# Integer 64
int_tensor = torch.tensor([1, 2], dtype=torch.int64)
print(int_tensor)

# Boolean
bool_tensor = torch.tensor([True, False], dtype=torch.bool)
print(bool_tensor)