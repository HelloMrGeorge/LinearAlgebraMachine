import __init__
import sympy as sp
from lam.quad.quadratic import QuadSolver

import logging
logging.basicConfig(level=logging.DEBUG)

mat = sp.Matrix([
    [1,3,4,6],
    [3,2,3,0],
    [4,3,7,8],
    [6,0,8,10]
])
solver = QuadSolver(mat)
# m = solver.get_standardFrom()
logging.debug(solver.get_course())
