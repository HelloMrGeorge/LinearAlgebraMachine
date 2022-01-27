import sympy as sp
from lam.core.solver import matSolver
from sympy import MutableDenseMatrix

class LinequSolver:
    '''
    线性方程组Ax = b的求解器
    '''
    def __init__(self, mat: MutableDenseMatrix, vec : MutableDenseMatrix) -> None:
        self.mat: MutableDenseMatrix = mat # 方程左端的矩阵A
        self.vec: MutableDenseMatrix = vec # 方程右端的常数项b