import torch

#자동미분 -> autograd
#backpropagation을 위한 미분 계산

x = torch.ones(3, 3, requires_grad=True)

y = x + 5
print(y)

print(y.grad_fn)

z = y * y * 2

out = z.mean()

print(z, out) #백워드에 대한 속성이 추가로 붙음

a = torch.randn(3, 3)
a = ((a * 3) / (a - 1))
print(a.requires_grad)

a.requires_grad_(True)
print(a.requires_grad)

b = (a * a).sum()
print(b.grad_fn)

#Gradient

out.backward()

print(x.grad)

x = torch.randn(3, requires_grad=True)

y = x * 2
while y.data.norm() < 1000:
    y *= 2

print(y)

v = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float)
y.backward(v)
print(y)
print(x.grad)


print(x.requires_grad)
y = x.detach()
print(y.requires_grad)
print(x.eq(y),all(y))

# a -> b -> c -> out

import torch

a = torch.ones(2, 2)
print(a)

a = torch.ones(2, 2, requires_grad=True)
print(a)

print("a.data: ", a)
print("a.grad: ", a.grad)
print("a.grad_fn: ", a.grad_fn)

b = a + 2
print(b)

c = b ** 2
print(c)

out = c.sum()
print(out)

out.backward()

print("a.data: ", a)
print("a.grad: ", a.grad)
print("a.grad_fn: ", a.grad_fn)

print("b.data: ", b)
print("b.grad: ", b.grad)
print("b.grad_fn: ", b.grad_fn)
import matplotlib
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

matplotlib.use("TkAgg")
nn.Conv2d(in_channels=1, out_channels=20, kernel_size=5, stride=1)

layer = nn.Conv2d(1, 20, 5, 1).to(torch.device('cpu'))
layer

weight = layer.weight
print(weight.shape)

weight = weight.detach()
weight = weight.numpy()

plt.imshow(weight[0, 0, :, :], "jet")
plt.colorbar()
plt.show()


