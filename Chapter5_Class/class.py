
#객체만들기

class Cookie:
    pass

a = Cookie()
b = Cookie()

#객체 vs 인스턴스
#인스턴스 -> 특정객체가 어떤 클래스의 객체인지 보여주기 위한것.
#a는 쿠키의 인스턴스임
#a는 객체임
#cookie는 클래스임

#사칙연산 객체만들기

#FourCal type객체를 생성할 때 생성한 객체는 메서드를 호출할때 자동으로 전달된다.

#생성자(Constructor)

#객체의 초기값을 설정하는 것으로 생각하면 된다.
#즉 객체가 생성될때 자동으로 호출되는 메서드를 의미한다.

# a = 클래스(초기인수1, 초기인수2, ...) <- 이형태로 작성한다.
# 클래스내에서는 __init__형태로 구현이 된다. 파이썬 생성자의 고유표현이다.

class FourCal():
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

a = FourCal(4, 2)

print(a.add())
