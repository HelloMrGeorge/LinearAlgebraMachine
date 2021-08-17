import numpy
from lam.core import gausselim,core,interpreter
from lam.det import det

a = '0,0,1,1;0,3,4,3;0,4,5,8;1,1,1,3'
b = interpreter.interpret(a)
# c = gausselim.gaussElim(b)
# c.print()
print(b)
c = det.laplaceExpand(b,1)
c.print()
# print(b.cofactorMat(0,0))
