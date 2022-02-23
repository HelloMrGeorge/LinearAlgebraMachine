from latex.latextrans import *
from sympy import MutableDenseMatrix, Expr


def matParser(x: str) -> MutableDenseMatrix:
    return standard_transformation(latextrans(x))

def exprParser(x: str) -> Expr:
    return standard_transformation(x)
