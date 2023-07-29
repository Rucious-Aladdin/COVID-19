import re

p = re.compile("^python\s\w+", re.M) # ^, $의 메타문자를 문자열의 각 줄마다 적용해 줌.

data = """python one
life is too short
python two
you need python
python three
"""

print(p.findall(data))

charref = re.compile(r"""
&[#] #start of a numeric entity reference
(
0[0-7]+ #Octal form
|[0-9]+ #Decimal form
|x[0-9a-fA-F]+ #Hexadecimal form
)
;
""", re.VERBOSE)


p = re.compile("\\section") #\\두개가 \한개를 의미함.
p = re.compile(r"\\section") #\를 4번을 적을 필요가 없음.
