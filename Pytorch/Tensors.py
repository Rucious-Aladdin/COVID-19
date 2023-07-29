import torch
import numpy as np

data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
print(x_data)

np_array = np.array(data)
x_np = torch.from_numpy(np_array)
print(x_np)

x_ones = torch.ones_like(x_data)
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float)
print(f"Random Tensor: \n {x_rand} \n")

shape = (2, 3, )
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor} \n")

tensor = torch.rand(3, 4)

print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device of tensor: {tensor.device}")

if torch.cuda.is_available():
    tensor = tensor.to("cuda")

tensor = torch.ones(4, 4)
print(f"First row: {tensor[0]}")
print(f"First column: {tensor[:, 0]}")
print(f"Last Column: {tensor[..., -1]}")
tensor[:, 1] = 0
print(tensor)

t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(f"t1 :{t1}")

y1 = tensor @ tensor.T # T는 전치행렬, @는 행렬곱 연산 기호
y2 = tensor.matmul(tensor.T)
print(f"y1 :{y1}")
print(f"y2 :{y2}")

y3 = torch.rand_like(y1)
torch.matmul(tensor, tensor.T, out=y3)
print(f"y3 :{y3}")


z1 = tensor * tensor
z2 = tensor.mul(tensor)
print(z1)
print(z2)

z3 = torch.rand_like(tensor)
torch.mul(tensor, tensor, out=z3)


print(z3)

agg = tensor.sum()
agg_item = agg.item()
print(agg_item, type(agg.item))

print(f"{tensor} \n")
tensor.add_(5)
print(tensor)

