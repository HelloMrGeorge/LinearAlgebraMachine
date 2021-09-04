from lam.linearEqu import GE
from lam.core import output, ndmatrix, expression
import numpy as np

class LinearEqu(expression.Equation):

    def __init__(self, Ab: ndmatrix.NumMatrix) -> None:
        self.Ab = Ab
        self.A = Ab[:, 0:2]
        self.b = Ab[:, 3]
        self.left = self.A
        self.right = self.b
        return

def SLEbyStep(equ: LinearEqu):
    mat = equ.Ab
    if (mat[-1, :-1] == 0).all() and mat[-1, -1] != 0:
        return 'no solution'
    indOfnoz = np.ones((1, mat.shape[0]))*-1
    for rowInd in range(mat.shape[0]):
        for colInd in range(mat):
            pass
    return


class SLEIterator():
    '''
    解线性方程的迭代器对象
    '''
    def __init__(self, equ: LinearEqu) -> None:
        self.equ = equ
        return

    def __iter__(self):
        return self

    def __next__(self):
        pass

# def solveOfMat(A: ndmatrix.NumMatrix, b: ndmatrix.NumMatrix):
#     '''
#     输入参数为矩阵类型的线性方程求解函数
#     Parameters: A: ndmatrix.NumMatrix
#                     待展开的矩阵
#                 b: ndmatrix.NumMatrix
#                     展开行或列的序号，序号从零开始。
#     Returns:    expr: expression.Polynomial
#                     返回计算结果的多项式对象
#     '''
#     A = righ
#     equMat = np.stack
#     return mat

# def solveLEqu(equ: Equation) -> ndmatrix.NumMatrix:
#     mat = solveOfMat(equ.left, equ.right)
#     return mat