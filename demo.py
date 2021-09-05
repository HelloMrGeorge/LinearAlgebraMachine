import sympy as sp
from lam.linearequation import reduction, solve, outtext
from lam.determinant import determinant
from lam.printing import latextext
a = sp.Matrix([
    [0,0,1,0],
    [0,2,5,8],
    [3,2,4,0],
])
# co = solve.EquationSolve(a)
# co.get_course()
# for i in co.course:
#     print(sp.latex(i))
a = determinant.Determinant(a)
b = a.minor_subdet(0,0)

