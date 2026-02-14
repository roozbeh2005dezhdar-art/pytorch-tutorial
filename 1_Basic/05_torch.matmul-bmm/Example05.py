import torch

# bmm vs matmul for batches
batch_A = torch.randn(2, 3, 4)
batch_B = torch.randn(2, 4, 5)

result_bmm = torch.bmm(batch_A, batch_B)
result_matmul = torch.matmul(batch_A, batch_B)

print("bmm result shape:", result_bmm.shape)
print("matmul result shape:", result_matmul.shape)
print("Are they equal?", torch.allclose(result_bmm, result_matmul))


#Function	Input Dimensions	Batching Support	Broadcasting
# mm	         2D only	         ❌ No         	❌ No
# bmm	         3D only	    ✅ Yes (explicit)	❌ No
# matmul	    Any (≥1D)	   ✅ Yes (automatic)	✅ Yes
