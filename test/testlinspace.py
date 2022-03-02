from cgi import test
import __init__
import sympy as sp
from lam.linspace.MLIG import MLIGSolver
from lam.linspace.lincombination import LincombinationSolver
from lam.linspace.linspace import LinDependenceSolver

ma = sp.Matrix([[1,2,3,-1], [3,2,1,-1], [2,3,1,1], [2,2,2,-1], [5,5,2,0]])
mb = sp.Matrix([[1,2,3], [3,2,1], [0,0,0]])
vec = sp.Matrix([[-1],[-1],[0]])

def test1():
    for i in range(len(ma)):
        ma[i] = sp.Matrix(ma[i])
    solver = MLIGSolver(ma)
    print(solver.dict())

def test2():
    rs = sp.linsolve(ma)
    print(rs.is_empty)

def test3():
    sl = LincombinationSolver(mb, vec)
    dc = sl.dict()
    print(dc['solveset'])

def test4():
    sl = LinDependenceSolver(ma)
    dc = sl.dict()
    print(dc['result'])
    print(dc['GES'])

if __name__ == "__main__":
    test4()
