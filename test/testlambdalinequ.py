import sympy as sp
from sympy.abc import a
from sympy import S, sqrt, RR
import lambdalinequ

def testFactor():
    mat = [
        [a, 1, 1],
        [1, a, 1],
        [1, 1, a],
    ]
    mat = sp.Matrix(mat)
    deter = mat.det()
    print(deter)
    # sset = sp.solveset(deter)
    # print(sset)
    fd = sp.factor(a**2 + 2, domain=RR)
    print(fd)

def testSubs():
    mat = [
        [a, 1, 1],
        [1, a, 1],
        [1, 1, a],
    ]
    mat = sp.Matrix(mat)
    print(mat.subs(a, 2))

def testlambdalinequ():
    mat = [
        [a, 1, 1, 1],
        [1, a, 1, a],
        [1, 1, a, a**2],
    ]
    mat = sp.Matrix(mat)
    solver = lambdalinequ.Lambda_linsolver(mat, a)
    print(solver.solveset)
    print(solver.elimination_course)

if __name__ == "__main__":
    testlambdalinequ()
