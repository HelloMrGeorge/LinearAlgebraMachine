import numpy as np
import sympy as sp
from lam.linearequation import reduction
# from lam.linearequation import reduction
# from lam.core import ndmatrix, input, output, expression
# from lam.det import det

# a = '1,1,2,1;0,3,4,1;0,3,4,3;1,3,4,6'
# a = input.Interpreter.intepretAs('Determinant', a)
# equ1 = expression.Equation('1+1', '2')
# equ2 = expression.Equation('2+1', '3')
# equGp = expression.EquGroup()
# equGp.append(equ1)
# equGp.append(equ2)
# print(equGp.htmlStr())

a = sp.Matrix([
    [0,2,3,4],
    [0,4,5,6],
    [0,5,7,8],
    [0,3,5,6],
])
co = reduction.MatrixReduction(a)
course = co.echelon_form()
for x in course:
    print(sp.latex(x))
