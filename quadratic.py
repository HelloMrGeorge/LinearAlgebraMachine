import logging
from typing import List, Tuple
import sympy as sp
from sympy.matrices.dense import MutableDenseMatrix
from lam.core.solver import matSolver

logging.basicConfig(level=logging.DEBUG)

course_type = List[Tuple[MutableDenseMatrix, MutableDenseMatrix]]

class QuadSolver(matSolver):

    def __init__(self, mat: MutableDenseMatrix) -> None:
        matSolver.__init__(self, mat)
        self.course: course_type = []
        self.is_symmetry: bool = True if self.mat.is_symmetric() else False

    def get_course(self) -> course_type:
        return self.course

    def quad_term_trans(self, i: int) -> MutableDenseMatrix:
        # 配方平方项的线性变数替换，i表示平方项的下标
        ret: MutableDenseMatrix = sp.eye(self.dim)
        for k in range(self.dim):
            if k != i:
                ret[i, k] = -sp.Rational(self.mat[i, k], self.mat[i, i])
        return ret

    def cross_term_trans(self, i: int , j:int) -> MutableDenseMatrix:
        # 消去交叉项的线性变数替换，i，j表示交叉项的下标a_{ij}
        if i == j:
            raise Exception("不是交叉项")
        ret: MutableDenseMatrix = sp.eye(self.dim)
        ret[i,i], ret[j,j], ret[i,j], ret[j,i] = 1, -1, 1, 1
        return ret

    def get_standardFrom(self) -> MutableDenseMatrix:
        pass


if __name__ == "__main__":
    mat = sp.Matrix([
        [1,3,4],
        [3,2,3],
        [4,3,7],
    ])
    solver = QuadSolver(mat)
    a = solver.cross_term_trans(1,1)
    logging.debug(a)
