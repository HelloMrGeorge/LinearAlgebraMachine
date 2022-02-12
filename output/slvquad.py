import json
from lam.readtext.readtext import readtext
import sympy as sp
import sympy.core.numbers as nu
import numpy as np
from lam.quad.quadratic import *
def slvget_course(a:str):
    quadSorver=QuadSolver(readtext(a))
    m=quadSorver.get_course()
    print(m)
    m=sp.latex(m)
    return m
if __name__ == "__main__":
    print(slvget_course("[[1,3,4,6],[3,2,3,0],[4,3,7,8],[6,0,8,10]]"))

