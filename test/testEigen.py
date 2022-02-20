import __init__
from lam.eigen.eigenvalue import EigenSolver
import sympy as sp
import logging
logging.basicConfig(level=logging.DEBUG)

a = sp.Matrix([
    [1,1,1],
    [1,2,1],
    [1,1,1],
])

slv = EigenSolver(a)
v = slv.get_course()
v = v['charpoly']
logging.debug(v)