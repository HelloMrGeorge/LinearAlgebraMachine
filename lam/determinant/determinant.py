import sympy as sp
from lam.determinant import cofactor, laplaceexpand

class Deter(sp.matrices.dense.MutableDenseMatrix):
    '''
    Deter   创建行列式对象的类，没有写全名Determinant是因为会和sympy的某些类冲突
    继承sympy的MutableDenseMatrix，实现基本的行列式操作。
    在输出latex文本时，sympy未提供双竖线的行列式定界符，请在编辑网页文本时，自行修改，
    或使用printing子包的自定义latex模块。
    在打印latex文本时请使用关键字参数mat_delim = '|'，以实现双竖线输出。
    '''

    def cofactor_submatrix(self, i, j):
        return cofactor.cofactor_submatrix(self, i, j)
    
    def lap_expand(self, n: int = 1, coe = 1, axis: int = 0):
        return laplaceexpand.lap_expand(self, n, coe, axis)
    

def is_singular(mat: sp.MatrixBase) -> bool:
    assert mat.is_square
    return bool(mat.det() != 0)