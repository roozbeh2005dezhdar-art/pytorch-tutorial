import torch

# Mean with different dtypes
int_tensor = torch.tensor([1, 2, 3, 4], dtype=torch.int32)
mean_int = torch.mean(int_tensor.float())  # Need float for mean

print("Int tensor:", int_tensor)
print("Mean (converted to float):", mean_int)