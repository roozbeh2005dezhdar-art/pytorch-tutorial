import torch

# View vs Reshape (contiguous requirement)
tensor = torch.tensor([[1, 2, 3],
                       [4, 5, 6]])
transposed = tensor.T
print(transposed)
# view() may fail on non-contiguous tensors
try:
    will_fail = transposed.view(6)
    print("view() succeeded")
except RuntimeError as e:
    print("view() failed:", e)

# reshape() always works
will_work = torch.reshape(transposed, (6,))
print("reshape() succeeded:",will_work, will_work.shape)