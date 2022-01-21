from typing import List
from sympy.matrices.dense import MutableDenseMatrix

class matSolver:

    def __init__(self, mat: MutableDenseMatrix) -> None:
        self.mat: MutableDenseMatrix = mat
        self.course: List = []
        self.dim: int = mat.shape[0]

    def get_course(self) -> list:
        return self.course