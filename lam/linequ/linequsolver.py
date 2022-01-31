from typing import List
import sympy as sp
from sympy import MutableDenseMatrix
from lam.linequ.guasselimination import GESolver

class LinequSolver:
    '''
    线性方程组Ax = b的求解器
    '''
    def __init__(self, mat: MutableDenseMatrix, vec: MutableDenseMatrix) -> None:
        self.mat: MutableDenseMatrix = mat # 方程左端的矩阵A
        self.vec: MutableDenseMatrix = vec # 方程右端的常数项b
        self.Ab: MutableDenseMatrix = sp.Matrix.hstack(mat, vec) # A和b构成的扩增矩阵[A,b]
        self.elimination_course: List[MutableDenseMatrix] = [] # 存储阶梯化矩阵的过程
        self.solveset: tuple = () # 存储方程的解集

    
    def get_course(self) -> None:
        self.reduce_row()
        self.solve_echelon()

    def reduce_row(self) -> None:
        '''
        先进行矩阵阶梯化运算
        '''
        solver = GESolver(self.Ab)
        solver.get_course()
        self.elimination_course = solver.course
        self.Ab = self.elimination_course[-1]

    def solve_echelon(self) -> None:
        '''
        解出reduce_row(self)得到的阶梯型矩阵
        '''
        self.solveset = sp.linsolve(self.Ab)
        if self.solveset.is_empty == False: # 注意，如果解集为空，solveset就是空集对象，而不是tuple类型
            self.solveset =  self.solveset.args[0]