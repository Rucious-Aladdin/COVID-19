from Chapter5_Class.game import mod2
import sys
import os

print(mod2.PI)

a = mod2.Math()
print(a.solv(2))

print(sys.path)
cwd = os.getcwd()


sys.path.append(cwd)
print(sys.path)
