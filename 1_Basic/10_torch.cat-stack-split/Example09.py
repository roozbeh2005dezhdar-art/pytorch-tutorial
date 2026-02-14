import torch

# Split along different dimensions
matrix = torch.tensor([[1, 2, 3, 4],
                       [5, 6, 7, 8]])

split_rows = torch.split(matrix, 1, dim=0)  # Split each row
split_cols = torch.split(matrix, 2, dim=1)  # Split into 2-column chunks

print("Original:\n", matrix)
print("Split rows (dim=0):")
for s in split_rows:
    print("  ", s)

print("Split cols (dim=1):")
for s in split_cols:
    print("  ", s)