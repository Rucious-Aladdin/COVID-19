import sys

print(sys.argv)
print(sys.path)
sys.path.append(sys.path[0][:-8] + "/game")
print(sys.path)

"""
import mod2
print(mod2.add(2, 4))
"""

import pickle

f = open("test.txt", "wb")
data = {1: "python", 2: "you need"}
pickle.dump(data, f) #객체 직렬화, 저장
f.close()

f = open("test.txt", "rb") #바이너리 스트림으로 연결되므로 일반 읽기 모드로 사용할수 없음에 주의.
data = pickle.load(f)
print(data)

import os

print(os.environ)
print(os.environ["PATH"])
print(os.getcwd())
print(os.system("ls -al"))

f = os.popen("ls -al")
print(f.read())

#mkdir, rmdir, unlink(파일 삭제), rename(src, dst) 등이 있다.

import shutil #파일 복사 모듈

shutil.copy("test.txt", "dst.txt")

import glob #디렉토리의 파일 전부를 리스트로 만듬

print(glob.glob("%s%s" % (os.getcwd(), "/*")))

import tempfile

filename = tempfile.mkstemp()
print(filename)

import time

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())

time.strftime('%x', time.localtime((time.time())))
time.strftime("%c", time.localtime(time.time()))
"""
for i in range(10):
    print(i)
    time.sleep(0.2)
"""

import calendar

print(calendar.calendar(2015))
print(calendar.weekday(2015, 12, 31))
print(calendar.monthrange(2015, 12))

import random

a = random.random()
print(a)

import random

def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)

"""
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))
"""

import webbrowser
"""
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com")
"""
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []

for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()