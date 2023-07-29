import torch

#초기화 되지 않은 행렬

x = torch.empty(4, 2)
print(x)

#무작위로 초기화된 행렬

x = torch.rand(4, 2)
print(x)

#dtype이 long으로 채워진 텐서

x = torch.zeros(4, 2, dtype=torch.long)
print(x)

x = torch.tensor([3, 2.3])
print(x)

x = x.new_ones(2, 4, dtype=torch.double)
print(x) #double이 float64fh 매칭

x = torch.rand_like(x, dtype=torch.float) #랜던값으로 채우고, 타입을 플로트로 지정함.
print(x)

print(x.size())

#텐서의 연산

print(x)

y = torch.rand(2, 4)
print(y)

#덧셈
print(x + y)

print(torch.add(x, y))

result = torch.empty(2, 4)
torch.add(x, y, out=result) # out인자를 줄수 있음

print(result)

y.add_(x)
print(y) # y += x

x = torch.Tensor([[1, 3], [5, 7]])
y = torch.Tensor([[2, 4], [6, 8]])

print(x - y)
print(torch.sub(x, y))
print(x.sub(y))

#곱셈

print(x*y)
print(torch.mul(x, y))

#나눗셈

print(x / y)
print(torch.div(x, y))

#내적(행렬곱)

print(torch.mm(x, y))

#인덱싱

print(x)
print(x[:, 1])

#view기능

x = torch.randn(4 ,5)
y = x.view(20)
z = x.view(5, -1) # "-1" 부분은 자동으로 결정

print(x)
print(y)
print(z)

#item

x = torch.randn(1)
print(x)
print(x.item()) #스칼라값 하나만 존재해야함.
print(x.dtype)

"""
x = torch.randn(2)
print(x)
print(x.item()) -> 2개의 엘리먼트 존재, 오류 발생
print(x.dtype)
"""

tensor = torch.rand(1, 3, 3)

t = tensor.squeeze() #차원을 축소하는 기능
print(t)

#unsqueeze, 차원을 증가시킴.

t = tensor.unsqueeze(dim=0)

print(t)

#stack, 텐서간 결합

x = torch.FloatTensor([1, 4])
y = torch.FloatTensor([2, 5])
z = torch.FloatTensor([3, 6])

print(torch.stack([x, y, z]))

#cat, concatnate

a = torch.randn(1, 3, 3)
b = torch.randn(1, 3, 3)
c = torch.cat((a, b), dim=2)

print(c)
print(c.size())

#chunk -> 텐서를 여러개로 나눌때 사용

tensor = torch.rand(3, 6)
t1, t2, t3, t4, t5, t6 = torch.split(tensor, 1, dim=1)

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)

#torch, numpy는 서로 호환이 가능함.

import numpy as np

a = np.ones(7)
b = torch.from_numpy(a)

np.add(a, 1, out=a)
print(a)
print(b) #서로 공유된 메모리임을 확인이 가능함.

#CUDA tensor

import torch

x = torch.rand(1)
print(x)
print(x.item())
print(x.dtype)

device = torch.device("cude" if torch.cuda.is_available() else "cpu")
print(device)

y = torch.ones_like(x, device=device)
x = x.to(device)
z = x + y
print(device)
print(z)
print(z.to("cpu", torch.double))

#nn & nn.functional

#두 패키지가 같은 기능, 방식은 다름
#autograd관련 작업을 위 패키지를 이용해 처리
#requires_grad

#가중치, 편향 값들이 내부에서 자동으로 생성되는 레이어들을 사용할때 이용.
#nn.functional 패키지

import torch
import torch.nn as nn

m = nn.Conv2d(16, 33, 3, stride=2)

m = nn.Conv2d(16, 33, (3, 5), stride=(2, 1), padding=(4, 2), dilation=(3, 1))

input = torch.randn(20, 16, 50 ,100)
output = m(input)
print(output.shape)
print(output)

#nn.functional 패키지

#전부 function으로 활용됨


import torch
import torch.nn.functional as F

filters = torch.randn(8, 4 , 3, 3)
inputs = torch.randn(1, 4, 5, 5)
conv = F.conv2d(inputs, filters, padding=1)
print(conv.shape)

#Torch vision

# -> tranforms , 전처리 메소드

import torch
import torchvision
import torchvision.transforms as transforms

transform = transforms.Compose([transforms.ToTensor(),
                               transforms.Normalize(mean=(0.5,), std=(0.5, ))])
import torch
from torch.utils.data import Dataset, DataLoader

import torchvision
import torchvision.transforms as transforms
import os

cwd = os.getcwd()

trainset = torchvision.datasets.MNIST(root=cwd,
                                      train = True,
                                      download = True,
                                      transform=transform)

testset1 = torchvision.datasets.MNIST(root=cwd,
                                     train=False,
                                     download=True,
                                     transform=transform)



train_loader = DataLoader(trainset, batch_size = 8, shuffle=True, num_workers=2)
test_loader = DataLoader(testset1, batch_size=8, shuffle=True, num_workers=2)

dataiter = iter(train_loader)
images, labels = dataiter.next()
print(images.shape, labels.shape) #채널이 앞에 출력됨
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")
plt.style.use('seaborn-white')

torch_image = torch.squeeze(images[0])
print(torch_image.shape)

image = torch_image.numpy()

label = labels[0].numpy()
print(label.shape)

plt.title(label)
plt.imshow(image, 'gray')
plt.show()


label = labels[0].numpy()
print(label.shape)

plt.title(label)
plt.imshow(image, 'gray')
plt.show()