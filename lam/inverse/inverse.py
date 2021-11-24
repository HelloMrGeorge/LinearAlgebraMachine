from typing import List
import sympy as sp
from sympy.matrices.dense import MutableDenseMatrix

import logging
logging.basicConfig(level=logging.DEBUG)

class InverseSolver:

    def __init__(self,mat) -> None:
        self.mat: MutableDenseMatrix = mat
        self.dim = self.mat.shape[0]
        self.course: List[MutableDenseMatrix] = []
        self.is_Invertible = False if self.mat.det() == 0 else True #可逆标志

    def getInverse(self) -> List[MutableDenseMatrix]:
        if self.is_Invertible == False:
            raise Exception('矩阵不可逆')

        self.course.clear()
        mat = self.mat.copy()
        AE: MutableDenseMatrix = mat.row_join(sp.eye(self.dim)) #将原矩阵与单位矩阵连接，用Gauss-Jordan消元法求逆
        self.course.append(AE)

        #Gauss消元
        for pivot_rowInd in range(self.dim-1): #最后一行不用选主元
            pivot = AE[pivot_rowInd, pivot_rowInd]
            #选主元，如果待消元的列不为0，则选为主元，否则选最开始一行的元素为主元
            if pivot == 0:
                for rowInd in range(pivot_rowInd+1, self.dim):
                    if AE[rowInd, pivot_rowInd] != 0:
                        AE = AE.elementary_row_op(op="n<->m", row1=pivot_rowInd, row2=rowInd)
                        self.course.append(AE.copy())
                        break
            #用主元所在的行消元
            for rowInd in range(pivot_rowInd+1, self.dim):
                if AE[rowInd, pivot_rowInd] != 0:
                    k = -sp.Rational(AE[rowInd, pivot_rowInd], pivot)
                    AE = AE.elementary_row_op(op='n->n+km', k=k, row1=rowInd, row2=pivot_rowInd)
                    self.course.append(AE.copy())

        #Jordan消元
        for pivot_rowInd in range(self.dim-1, 0, -1): #第一行不用选主元
            pivot = AE[pivot_rowInd, pivot_rowInd]
            #先将主元化为1
            if pivot != 1:
                AE = AE.elementary_row_op(op='n->kn', k=sp.Rational(1, pivot), row=pivot_rowInd)
                self.course.append(AE.copy())
            #用主元所在的行消元
            for rowInd in range(pivot_rowInd-1, -1, -1):
                if AE[rowInd, pivot_rowInd] != 0:
                    k = -AE[rowInd, pivot_rowInd]
                    AE = AE.elementary_row_op(op='n->n+km', k=k, row1=rowInd, row2=pivot_rowInd)
                    self.course.append(AE.copy())
        return self.course

if __name__ == '__main__':
    mat = sp.Matrix([[1,3,3],[3,2,1],[2,3,3]])
    logging.info(mat)
    solver = InverseSolver(mat)
    co = solver.getInverse()
    logging.info(co)
    logging.info(mat.inv())