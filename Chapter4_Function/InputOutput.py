import os

cwd = os.getcwd()
print(cwd)

#파일 생성
f = open("%s/새파일.txt" % cwd, "w")

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

f.close()

#파일 읽기

#파일에 새로운 내용 추가하기

f = open("%s/새파일.txt" % cwd, "a")

for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

f.close()

# with문과 함께 사용하기 -> 파일을 열고 닫는 것을 자동으로 처리하는 파이썬의 기능

with open("%s/foo.txt" % cwd, "w") as f:
    f.write("Life is too short, you need python")

#sys 모듈로 매개변수를 주는 법

import sys

args = sys.argv[1:]
for i in args:
    print(i)

