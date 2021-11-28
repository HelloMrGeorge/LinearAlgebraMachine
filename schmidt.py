from sympy.matrices.dense import MutableDenseMatrix
from lam.core.solver import matSolver

import logging
logging.basicConfig(level=logging.DEBUG)

class schmidtOrthogonalizer(matSolver):
    '''
    Schmidt正交化求解器
    '''
    def __init__(self, mat: MutableDenseMatrix) -> None:
        super().__init__(mat)
        self.dim = mat.shape

    def get_course(self) -> list:
        return super().get_course()