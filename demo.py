import numpy as np
from lam.core import ndmatrix, GE, input, output, expression
from lam.det import det

a = '1,1,2,1;0,3,4,1;0,3,4,3;1,3,4,6'
a = input.Interpreter.intepretAs('Determinant', a)

mono = expression.Monomial(a)
poly = expression.Polynomial()
poly.append(mono)

for i in det.LEIterator(poly):
    print(i.htmlStr())