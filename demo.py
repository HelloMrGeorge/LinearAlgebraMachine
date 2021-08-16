import numpy
from lam.core import gausselim,core
from lam.det import det

a = '1,1,1;1,3,4;0,4,5'
b = core.interpret(a)

print(det.triDet(b))
print(numpy.linalg.det(b))





