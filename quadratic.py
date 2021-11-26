import logging
from typing import List, Tuple
import sympy as sp
from sympy.matrices.dense import MutableDenseMatrix
from lam.core.solver import matSolver
from lam.quad.quadbase import *
from quadbase import is_complete_square

logging.basicConfig(level=logging.DEBUG)

course_type = List[Tuple[MutableDenseMatrix, MutableDenseMatrix]]

def cross_term_trans(mat: MutableDenseMatrix, i: int , j:int) -> MutableDenseMatrix:
    # 消去交叉项的线性变数替换，i，j表示交叉项的下标a_{ij}
    if i == j:
        raise Exception("不是交叉项")
    ret: MutableDenseMatrix = sp.eye(mat.shape[0])
    ret[i,i], ret[j,j], ret[i,j], ret[j,i] = 1, -1, 1, 1
    return ret

class QuadSolver(matSolver):

    def __init__(self, mat: MutableDenseMatrix) -> None:
        matSolver.__init__(self, mat)
        self.course: course_type = []
        self.is_symmetry: bool = True if self.mat.is_symmetric() else False

    def get_course(self) -> course_type:
        return self.course

    def get_standardFrom(self) -> MutableDenseMatrix:
        if self.is_symmetry == False:
            raise Exception('不是对称矩阵')
        
        mat = self.mat.copy()
        
        return mat


if __name__ == "__main__":
    mat = sp.Matrix([
        [1,3,4],
        [3,2,3],
        [4,3,7],
    ])
    T = cross_term_trans(mat, 0,1)
    logging.debug(T)
