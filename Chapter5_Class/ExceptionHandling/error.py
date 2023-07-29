"""

오류는 언제 생기는가?

1. 없는 파일을 참조하였을때 -> FileNotFound 에러 발생
2. 0으로 나눌때 -> ZeroDivisionError 발생
3. 배열/리스트의 크기를 넘어선 원소를 참조할때 -> IndexError 발생


"""

#try, except문을 이용해 오류 발생시 프로그램이 종료되지 않고 계속 수행되도록 만들 수 있다.


"""
try:
    ...
except[발생 오류[as 오류 메세지 변수]]:
    ...

"""

try:
    4 / 0
except ZeroDivisionError as e: # 오류종류가 Zero~에 저장, 오류 메세지가 e에 저장됨.
    print(e)

f = open("foo.txt", 'w')

try:
    pass
finally:
    f.close()

#여러 오류의 처리
"""
try:
    a = [1, 2]
    print(a[3])
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

"""

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e: #2개 이상의 오류를 묶어서 처리함.
    print(e)

#try문에 else를 사용할 수도 있음.

while True:
    try:
        age = 20
    except:
        print("입력이 정확하지 않습니다.")
    else:
        if age <= 18:
            print("미성년자는 출입 금지입니다.")
        else:
            print("환영합니다.")
        break

#오류 회피하기

try:
    f = open("나 없는 파일 응애", "r")
except FileNotFoundError:
    pass

#오류를 일부러 발생시키는 경우!

class Bird:
    def fly(self):
        raise NotImplementedError #자식 클래스가 fly함수를 오버라이딩 하지 않은 경우 오류가 발생!
        #raise는 오류를 강제로 발생시키는 예약어임.
class Eagle(Bird):
    def fly(self):
        print("very fast")
    #fly함수를 오버라이딩해서 정의해주면 문제가 발생하지 않음.

eagle = Eagle()
eagle.fly()

