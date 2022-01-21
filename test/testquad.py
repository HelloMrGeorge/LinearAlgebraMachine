import __init__
import sympy as sp
from lam.quad.quadratic import QuadSolver

import logging
logging.basicConfig(level=logging.DEBUG)



def test1():
    mat = sp.Matrix([
    [1,3,4,6],
    [3,2,3,0],
    [4,3,7,8],
    [6,0,8,10]
    ])
    solver = QuadSolver(mat)
    co = solver.get_course()
    newco = []
    for i in co:
        newco.append(sp.latex(i[0]))
        newco.append(sp.latex(i[1]))
    logging.debug(newco)

if __name__ == '__main__':
    test1()