import sympy as sp
from sympy.matrices.dense import Matrix
from sympy.testing.runtests import test

def testIsSingular():
    a = sp.symbols('a')
    mat = sp.diag(*[1 for i in range(3)])
    mat = Matrix.hstack(mat, mat)
    print(a*0, bool(a*0), mat)
    return

testIsSingular()