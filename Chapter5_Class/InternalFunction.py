print(abs(-3))

#all -> 반복 가능한 자료에 거짓인 자료가 하나라도 있으면 False, 나머지느 True

print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))

#any -> 반복가능한 자료에 하나라도 참이 있으면 True를 출력

print(any([0,0,0,0]))
print(any([1, 0, 0, 0]))

#chr -> 유니코드 값(숫자)를 입력받아 문자로 변환(int)

chr(97)
chr(44032)

#dir -> 객체가 자체적으로 가진 변수, 함수를 보여줌

print(dir([1, 2, 3]))
print(dir({'1' : 'a'}))

#divmod -> 2개의 숫자를 입력받아 몫, 나머지를 튜플로 반환

print(divmod(7, 3))

#enumerate -> 순서가 있는 자료형을 입력받아 인덱스 값을 포함하는 enumerate 객체를 돌려줌.

for i, name in enumerate(['body', "foo", "bar"]):
    print(i, name)

#eval -> 실행가능한 문자열을 입력받아 문자열을 실행한 결과를 돌려줌
    print(eval('1+2'))
    print(eval("divmod(4,3)"))

#filter -> 첫번째 인수를 함수에 집어넣어서 결과값이 참인 것만 묶어서 반환

def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

#hex -> 정수 값을 입력받아 16진수로 변환

print(hex(234))
print(hex(3))

#id -> 객체를 입력받아 고유 주소값을 반환

a = 3
print(id(a))


#input -> 사용자 입력을 받는 함수
"""
a = input()
b = input("Enter: ")
"""
#int -> 실수를 정수로 변환

print("3.4")

#isinstance

class Person: pass

a = Person()
print(isinstance(a, Person))

b = 3
print(isinstance(b, Person))

#list(s) -> 반복가능한 자료를 입력받아 리스트로 만들어 돌려주는 함수임.

print(list("python")) #문자 한개단위로 분리됨.

#map -> 함수와 반복가능한 자료를 입력으로 받아 각 요소를 함수에 집어넣고 실행한 결과를 묶어서 반환

def two_times(numberlist):
    result = []
    for number in numberlist:
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

def two_times2(x):
    return x * 2

print(list(map(lambda x : 2*x, [1, 2, 3, 4]))) #함수포인터, 리스트를 넘겨주고 결과를 반환

#max, min -> 반복가능한 자료형을 입력받아 그 최댓값, 최솟값을 돌려주는 함수

print(max([1, 2, 3]))
print(min([1, 2, 3]))

#oct -> 정수 형태의 숫자를 8진수로 바꾸어 돌려줌

print(oct(34))
print(oct(12345))

#open(filename, [mode]) -> mode생략시 read가 default값임
"""
f = open("binary_file", "rb")
fread = open("readmode.txt", 'r')
fread2 = open("read_mode.txt")
fappend = open("append_mode.txt", "a")
"""
#ord -> 문자의 유니코드를 돌려주는 함수 <-> chr()

print(ord('a'))
print(ord('가'))

#range([start, ], stop, [,step]) -> 범위 지정, start = 0, step = 1이 디폴트

print(list(range(5)))
print(list(range(5, 10)))
print(list(range(1, 10, 2)))

#round(number[, ndigits]) -> ndigits는 몇번째 자리까지 반올림할 것인지 넣어주는 인수, 디폴트는 0

print(round(4.6))
print(round(4.2))

#sorted -> 입력값을 정렬한 후 그 결과를 리스트로 돌려줌

print(sorted([1, 3, 2]))
print(sorted(["a", "b", "c"]))
print(sorted("zero"))

## 리스트 자료형의 sort는 객체그자체를 정렬만 시행, 결과를 반환하지는 않음.

#str -> 문자열 형태로 객체를 변환하여 돌려주는 함수임.

print(str(3))
print(str("hi"))
print(str("hi".upper()))

#sum -> 리스트, 튜플의 요소 합을 반환

print(sum([1, 2, 3]))
print(sum((4, 5, 6)))

#tuple ->자료형을 튜플로 변환

#type -> 입력값의 자료형을 반환

#zip -> 동일한 개수로 이루어진 자료형을 묶어줌.

print(list(zip("abc", "def")))

