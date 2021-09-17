import sympy as sp
from sympy.matrices.dense import Matrix, MutableDenseMatrix

def courseOfInverse(mat: sp.MatrixBase) -> list:
    assert is_singular(mat)
    #创建用于求逆的增广矩阵
    rectMat = sp.diag(*[1 for i in range(mat.shape[0])])
    rectMat = Matrix.hstack(mat, rectMat)
    return

def is_singular(mat: sp.MatrixBase) -> bool:
    assert mat.is_square
    return bool(mat.det())