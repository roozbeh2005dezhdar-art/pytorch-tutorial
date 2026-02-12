import torch

# With unbiased parameter (Bessel's correction)
data = torch.tensor([1.0, 2.0, 3.0, 4.0])

std_unbiased = torch.std(data, unbiased=True)  # Default for sample std
std_biased = torch.std(data, unbiased=False)   # For population std

print("Data:", data)
print("Unbiased std (sample):", std_unbiased)
print("Biased std (population):", std_biased)

# Sample standard deviation (correction=1):

# text
# σ = √[ Σ(x - μ)² / (n - 1) ]
# Used when data is a sample from a larger population

# Bessel's correction makes it unbiased

# Default behavior

# Population standard deviation (correction=0):

# text
# σ = √[ Σ(x - μ)² / n ]
# Used when data is the entire population

# No correction factor

# Use correction=0