def add(a, b):
    return a+b

a = 3
b = 4
sum = add(a, b)
print(sum)

def fibonaci(n):
    if n >= 3:
        return fibonaci(n-1) + fibonaci(n-2)
    elif n == 2:
        return 1
    else:
        return 0

sum = fibonaci(10)
print(sum)

print(add(b = 5, a = 4))

def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

sum = add_many(1, 2, 3, 4, 5, 6)
print(sum)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

result = add_mul("mul", 1, 2, 3, 4, 5)
print(result)

#kwargs 파라미터

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)

#초기값 설정
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27, False)
#초기화 하고싶은 변수는 뒤에 놓는다!

