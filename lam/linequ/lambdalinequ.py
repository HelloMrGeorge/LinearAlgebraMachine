# 讨论含单个参数的线性方程组

from typing import List
import sympy as sp
from sympy import MutableDenseMatrix, Symbol
from lam.linequ.linequsolver import LinequSolver

class Lambda_linsolver:
    
    def __init__(self, mat: MutableDenseMatrix, lam: Symbol, evaluate = True) -> None:
        '''
        求解含单个参数的线性方程组的求解器，
        设线性方程组为AX = b，参数mat代表其增广矩阵(A, b)，
        默认evaluate = True，即构造求解器后立即执行求解。
        '''
        self.mat: MutableDenseMatrix = mat # 给定一个待求解的增广矩阵
        self.lam: Symbol = lam # 用于告知求解器方程中参数的字母符号，比如lambda字母对应sympy.abc.lambda对象
        self.mA: MutableDenseMatrix = mat[:, :-1] # 线性方程组的系数矩阵A
        self.mb: MutableDenseMatrix = mat[:, -1] # 线性方程组的常数项
        self.evaluate = False
        
        if evaluate:
            self.get_course()
            self.evaluate = True

    def get_course(self) -> None:

        self.determinat = self.mA.det() # 保留A的行列式计算出的多项式
        self.factorization = sp.factor(self.determinat) # 保留self.determinat的因式分解式
        self.root = sp.solveset(self.determinat) # 保留多项式self.determinat的根

        if not self.root.is_empty: # 如果self.determinat有实根(默认实数)，则讨论行列式等于0的情况
            self.root: tuple = self.root.args
            self.solveset: list = [] # 用于存储每个根对应的线性方程组的解集
            self.elimination_course: List[MutableDenseMatrix] = [] # 用于存储每个根对应的线性方程组的消元过程
            
            for rt in self.root:
                solver = LinequSolver(self.mA.subs(self.lam, rt), self.mb.subs(self.lam, rt))
                self.solveset.append(solver.solveset)
                self.elimination_course.append(solver.elimination_course)

        # 行列式不等于0的情况
        solver = LinequSolver(self.mA, self.mb)
        self.solveset_nonzero = solver.solveset
        self.elimination_course_nonzeor = solver.elimination_course