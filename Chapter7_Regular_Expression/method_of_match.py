import re

p = re.compile("[a-z]+")

m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

#모듈단위로 수행

print(re.match("[a-z]+", "python")) #패턴 객체를 반복해서 사용할 필요가 없을때 위와 같이 사용

