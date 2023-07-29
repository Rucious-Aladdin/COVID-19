import re
p = re.compile("[a-z]+") #모든문자+ 의 정규식을 의미

m = p.match("python")
print(m)

m = p.match("3 python")
print(m)
"""

~작성 흐름도~

p = re.compile(정규표현식)
m = p.match("string goes here")
if m:
    print("Match found: ", m.group())
else:
    print("No match")

"""