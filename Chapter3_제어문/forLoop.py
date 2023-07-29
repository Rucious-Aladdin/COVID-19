test_list = ["one", "two", "three"]

for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]

for(first, last) in a:
    print(first + last)

#for문의 응용

marks = [90, 25, 67, 45, 80]

number = 0

for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

#for문과 continue

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

#range 함수의 이용

a = range(1, 11) #(시작 숫자, 끝 숫자)
print(a)

add = 0
for i in a:
    add = add + i

print(add)

#range 함수의 변환

marks = [90, 25, 67, 45, 80]

for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print('%d번 학생 축하합니다. 합격입니다.' % (number+1))

#구구단 작성하기

for i in range(2, 10):
    for j in range(1, 10):
        print("%3d" % (i*j), end=" ") #다음줄로 넘기지 않고 공백을 마지막으로 출력한 것임.
    print('')

#리스트 컴프리헨션

a = [1, 2, 3, 4]
result = [(num * 3) for (num) in a if (num % 2 == 0)]
print(result)
