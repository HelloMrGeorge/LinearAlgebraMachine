import logging
import sympy as sp
from sympy.matrices.dense import MutableDenseMatrix

logging.basicConfig(level=logging.DEBUG)

def is_square(mat: MutableDenseMatrix, i: int) -> bool:
    #判断平方项a_{ii}是否已经配方
    flag = True
    for k in range(mat.shape[0]):
        if k != i and mat[i, k] != 0:
            flag = False
            break
    return flag

def quad_term_trans(mat: MutableDenseMatrix, i: int) -> MutableDenseMatrix:
    # 配方平方项的线性变数替换，i表示平方项的下标
    dim = mat.shape[0]
    ret: MutableDenseMatrix = sp.eye(dim)
    for k in range(dim):
        if k != i:
            ret[i, k] = -sp.Rational(mat[i, k], mat[i, i])
    return ret

def cross_term_trans(mat: MutableDenseMatrix, i: int , j:int) -> MutableDenseMatrix:
    # 消去交叉项的线性变数替换，i，j表示交叉项的下标a_{ij}
    if i == j:
        raise Exception("不是交叉项")
    ret: MutableDenseMatrix = sp.eye(mat.shape[0])
    ret[i,i], ret[j,j], ret[i,j], ret[j,i] = 1, -1, 1, 1
    return ret

if __name__ == "__main__":
    mat = sp.Matrix([
        [1,3,4],
        [3,2,3],
        [4,3,7],
    ])
    T = cross_term_trans(mat, 0,1)
    logging.debug(T)