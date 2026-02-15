import torch

# Without no_grad (tracks gradients)
x = torch.tensor([1.0, 2.0], requires_grad=True)
y = x ** 2
loss = y.sum()
print(loss)
loss.backward()
print("Gradients:", x.grad)  # Gradients computed

# Visual Representation
# text
# x = [1.0, 2.0]
#        ↓    ↓
# y = x² → [1.0, 4.0]
#        ↓    ↓
# loss = sum(y) = 5.0

#---------------------

# When you call loss.backward(), PyTorch computes:

# ∂loss/∂x₁ = ∂loss/∂y₁ × ∂y₁/∂x₁ = 1 × 2x₁ = 2x₁ = 2.0

# ∂loss/∂x₂ = ∂loss/∂y₂ × ∂y₂/∂x₂ = 1 × 2x₂ = 2x₂ = 4.0

#(∂loss/∂yᵢ = ∂(y₁ + y₂ + ... + yᵢ + ... + yₙ)/∂yᵢ = 1))
#(∂(x₁²)/∂x₁ = 2x₁))