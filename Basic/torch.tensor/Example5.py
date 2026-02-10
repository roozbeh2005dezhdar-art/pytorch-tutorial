import torch

# For faster GPU transfer (needs GPU)
if torch.cuda.is_available():
    pinned = torch.tensor([1, 2], pin_memory=True)
    print(pinned)