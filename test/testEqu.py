import sympy as sp
from sympy.parsing.latex import parse_latex
import lam.linequ.guasselimination as guasselimination
import linequsolver

def test1():
    mat = [
        [1,sp.Rational(2,3),1,1],
        [3,1,1,1],
        [2,1,3,1],
    ]
    mat = sp.Matrix(mat)
    solver = guasselimination.GESolver(mat)
    solver.get_course()
    co = solver.course
    print(co)

def test2():
    mat = [
        [1,1,1],
        [1,1,1],
        [2,1,3],
    ]
    mat = sp.Matrix(mat)
    vec = [
        [1],
        [1],
        [2],
    ]
    vec = sp.Matrix(vec)
    solver = linequsolver.LinequSolver(mat, vec)
    solver.get_course()
    co1 = solver.elimination_course
    co2 = solver.solveset
    print(co1)
    print(sp.latex(co2))



if __name__ == "__main__":
    test2()