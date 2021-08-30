import numpy as np
from lam.core import ndmatrix, GE, input, output


a = '1,1,2,1;0,3,4,1;0,3,4,3;1,3,4,6'
a = input.interpret(a)
print(a)
for i in GE.GEIterator(a):
    print(i)
