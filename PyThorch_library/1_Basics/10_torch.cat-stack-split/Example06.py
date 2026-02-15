import torch

# Split tensor into equal chunks
tensor = torch.tensor([1, 2, 3, 4, 5, 6])
split_tensors = torch.split(tensor, 2)  # Split size 2

print("Split size 2:")
for i, t in enumerate(split_tensors):
    print(f"  Split {i}:", t)
# [1, 2], [3, 4], [5, 6]