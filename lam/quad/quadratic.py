import logging
from typing import List, Tuple
import sympy as sp
from sympy.matrices.dense import MutableDenseMatrix
from lam.core.solver import matSolver
from lam.quad.quadbase import *


logging.basicConfig(level=logging.DEBUG)

course_type = List[Tuple[MutableDenseMatrix, MutableDenseMatrix]]

class QuadSolver(matSolver):

    def __init__(self, mat: MutableDenseMatrix) -> None:
        matSolver.__init__(self, mat)
        self.course: course_type = []
        self.is_symmetry: bool = True if self.mat.is_symmetric() else False

    def get_course(self) -> course_type:
        self.get_standardFrom()
        return self.course

    def get_standardFrom(self) -> MutableDenseMatrix:
        # 获取mat的标准形
        if self.is_symmetry == False:
            raise Exception('不是对称矩阵')
        
        mat: MutableDenseMatrix = self.mat.copy()
        while mat.is_diagonal() == False:
            tran = next_quad_op(mat)
            logging.debug(f'tran: {tran}')
            mat = tran.T @ mat @ tran
            logging.debug(f'mat: {mat}') 
            self.course.append((tran.copy(), mat.copy()))
        return mat


if __name__ == "__main__":
    mat = sp.Matrix([
        [1,3,4,6],
        [3,2,3,0],
        [4,3,7,8],
        [6,0,8,10]
    ])
    solver = QuadSolver(mat)
    # m = solver.get_standardFrom()
    logging.debug(solver.get_course())
