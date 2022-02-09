import __init__
import sympy as sp
from lam.quad.quadratic import QuadSolver

import logging
logging.basicConfig(level=logging.DEBUG)



def test1():
    mat = sp.Matrix([
    [0,1,1,0],
    [1,0,-3,0],
    [1,-3,0,0],
    [0,0,0,3]
    ])
    solver = QuadSolver(mat)
    logging.debug(solver.result)
    logging.debug(solver.trans)
    logging.debug(solver.mark)

def test2():
    mat = sp.Matrix([
    [0,1,1,0],
    [1,0,-3,0],
    [1,-3,0,0],
    [0,0,0,3]
    ])
    solver = QuadSolver(mat)
    logging.debug(solver.dict())


if __name__ == '__main__':
    test2()