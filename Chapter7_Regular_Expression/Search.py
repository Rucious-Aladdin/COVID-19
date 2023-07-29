import re

p = re.compile("[a-z]+")

m = p.search("python")
print(m)

m = p.search("3 python")
print(m)

