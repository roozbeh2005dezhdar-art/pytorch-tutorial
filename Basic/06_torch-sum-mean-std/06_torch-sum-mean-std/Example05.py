import torch

# Standard deviation of all elements
tensor = torch.tensor([1.0, 2.0, 3.0, 4.0])
std_dev = torch.std(tensor)

print("Tensor:", tensor)
print("Standard deviation:", std_dev)

# # Step 1: Calculate mean
# mean = torch.mean(tensor)  # (1+2+3+4)/4 = 2.5

# # Step 2: Calculate squared differences from mean
# squared_diffs = (tensor - mean) ** 2  
# # [1-2.5=-1.5²=2.25, 2-2.5=-0.5²=0.25, 3-2.5=0.5²=0.25, 4-2.5=1.5²=2.25]

# # Step 3: Sum squared differences
# sum_squared_diffs = torch.sum(squared_diffs)  # 2.25+0.25+0.25+2.25 = 5.0

# # Step 4: Divide by (n-1) for sample std (Bessel's correction)
# variance = sum_squared_diffs / (len(tensor) - 1)  # 5.0 / 3 = 1.6667

# # Step 5: Take square root
# manual_std = torch.sqrt(variance)  # √1.6667 = 1.2909

# print(f"Manual calculation: {manual_std}")  # 1.2909
# print(f"torch.std: {std_dev}")             # 1.2909