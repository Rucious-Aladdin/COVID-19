#1번 문제

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#2번 문제

sum = 0
num = 0
while num != 1000:
    if num % 3 == 0:
        sum += num
    num += 1

print(sum)

#3번 문제
num = 1

while num != 6:
    for i in range(num):
        print("*", end="")
    print("")
    num += 1

#4번 문제

for i in range(1, 101):
    print("%4d" % i, end="")
    if i % 10 == 0:
        print("")

#5번 문제

scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

sum = 0
for score in scores:
    sum += score

avg = sum / len(scores)

print(avg)

#6번 문제

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1] #리스트 내포의 개념을 활용한 것
print(result)