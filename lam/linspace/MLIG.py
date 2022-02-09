# 极大线性无关组(MLIG) Maximal linearly independent group 

import sympy as sp
from typing import Any
from lam.linspace.lincombination import is_lincombination


class MLIGSolver:
    '''
    极大无关组求解器，注意为了兼容抽象的向量，构造方法中只能用列表装向量，不能直接用矩阵
    '''
    def __init__(self, group: list) -> None:
        self.group: list = group
        self.coefs: list = [] # 存储每次线性表示的系数
        self.MLIG: list = [] # 存储极大线性无关组
        self.position: list = [] # 存储极大线性无关组在group的位置

    def filtrate_MLIG(self) -> None: # 筛选法求极大线性无关组
        self.MLIG = [self.group[0]] # 请保证输入列表不为空
        self.position.append(0)
        for i in range(1, len(self.group)):
            coef = []
            flag = is_lincombination(self.MLIG, self.group[i], coef)
            self.coefs.append(coef)
            if not flag:
                self.MLIG.append(self.group[i])
                self.position.append(i)
        return

    def get_course(self) -> Any:
        self.filtrate_MLIG()
        return self

if __name__ == "__main__":
    A = [[1,2,3,-1], [3,2,1,-1], [2,3,1,1], [2,2,2,-1], [5,5,2,0]]
    for i in range(len(A)):
        A[i] = sp.Matrix(A[i])
    solver = MLIGSolver(A)
    co: MLIGSolver = solver.get_course()
    print(co.coefs)
    print(co.MLIG)