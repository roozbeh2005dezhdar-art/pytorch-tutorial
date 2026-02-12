import torch

# Practical: cross-entropy loss component
probs = torch.tensor([0.1, 0.7, 0.2])
log_probs = torch.log(probs)

print("Probabilities:", probs)
print("Log probabilities:", log_probs)
print("Negative log-likelihood:", -log_probs)