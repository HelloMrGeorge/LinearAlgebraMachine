from numpy import add
import sympy as sp
from lam.determinant import determinant

def lap_expand(matrix: determinant.Determinant, n: int, axis: int = 0):
    if axis == 0:   #0表示按行展开，否则按列展开
        expr = matrix.cofactor_subdet(n, 0)
        for colInd in range(1,matrix.shape[1]):
            t = sp.Mul(matrix[n, colInd], matrix.cofactor_subdet(n, colInd), evaluate = False)
            expr = sp.Add(expr, t, evaluate = False)
    else:
        expr = matrix.cofactor_subdet(0, n)
        for rowInd in range(1,matrix.shape[0]):
            t = sp.Mul(matrix[rowInd, n], matrix.cofactor_subdet(rowInd, n), evaluate = False)
            expr = sp.Add(expr, t, evaluate = False)
    return expr

def lapexp_expr(expr: sp.Expr) -> sp.Expr:
    pass
