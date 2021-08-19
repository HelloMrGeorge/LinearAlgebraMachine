import numpy as np
from lam.core import ndmatrix, gelim, input


a = '1,1,2;1,3,4;2,3,4'
a = input.interpret(a)
b = gelim.gaussElim(a)
print(b.htmlOutPut())
