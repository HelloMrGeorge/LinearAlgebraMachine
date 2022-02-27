import __init__
import sympy as sp
import lam.linequ.gausslimination as gausslimination
import lam.linequ.linequsolver as linequsolver

def test1():
    mat = [
        [0,1,1],
        [1,2,1],
        [1,1,2],
    ]
    mat = sp.Matrix(mat)
    solver = gausslimination.GESolver(mat)
    print(solver.course)

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
    co1 = solver.elimination_course
    co2 = solver.solveset
    print(co1)
    print(co2)



if __name__ == "__main__":
    test1()