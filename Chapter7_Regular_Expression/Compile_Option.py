#DOTALL(S) -> .이 줄바꿈 문자를 포함하여 모든문자와 매치될 수 있도록 함 <-> re.S
#IGNORECASE(I) -> 대소문자와 관계없이 매치할 수 있도록 함. <-> re.I
#MULTILINE(M) -> 여러줄과 매치 할수 있도록 함. <-> re.M
#VERBOSE(X) -> verbose모드를 사용할 수 있도록 함. <-> re.X

import re

p = re.compile("a.b")
m = p.match("a\nb")
print(m)

p = re.compile("a.b", re.S) #\n에 상관없이 검색할떄 많이 사용
m = p.match("a\nb")
print(m)

p = re.compile("[a-z]+", re.I)
print(p.match("python"))
print(p.match("PYTHON"))