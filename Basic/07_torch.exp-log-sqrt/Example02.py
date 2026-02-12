import torch

# Practical: softmax numerator
logits = torch.tensor([2.0, 1.0, 0.1])
exp_logits = torch.exp(logits)
print("Logits:", logits)
print("exp(logits):", exp_logits)
print("Softmax:", exp_logits / torch.sum(exp_logits))