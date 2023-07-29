#클래스의 상속

class FourCal():
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def add(self):
        result = self.first / self.second
        return result

#class 클래스 이름(상속할 클래스 이름)으로 작성

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

b = MoreFourCal(4, 2)

print(b.pow())

#상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경시에 사용함


#메서드 오버라이딩


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div())
