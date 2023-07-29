#mod1.py

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    print(add(1, 4))
    print(add(4, 2))

# __name__ 변수는 파이썬에서 내부적으로 이용되는 특별 변수이다.
# 셸에서 ModuleIntro를 실행하면 __name__에는 __main__이 저장된다.
# 그러나 ModuleUsing을 실행하면, 이파일이 임포트 되는 것이므로 __name__에 모듈이름이 저장이된다.