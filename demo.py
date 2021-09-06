import sympy as sp
from lam.linearequation import reduction, solve, outtext
from lam.determinant import determinant, laplaceexpand
from lam.printing import latextext
s1 = sp.symbols('s1')
a = sp.Matrix([
    [-1,3,1,0],
    [1,2,5,8],
    [3,2,4,0],
    [8,9,5,1],
])

a = determinant.Deter(a)
b = laplaceexpand.lapexp_expr(a)
b = laplaceexpand.lapexp_expr(b)
b = laplaceexpand.lapexp_expr(b)
print(b.doit())
