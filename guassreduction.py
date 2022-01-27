from typing import List
import sympy as sp
from sympy import MutableDenseMatrix

class GRSolver:
    '''
    执行高斯消元法的求解器
    '''

    def __init__(self, mat: MutableDenseMatrix) -> None:
        self.mat: MutableDenseMatrix = mat
        self.course: List[MutableDenseMatrix] = []

    def get_course(self):
        pass

    def reduce_row() -> None:
        pass