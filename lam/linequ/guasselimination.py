from typing import List
import sympy as sp
from sympy import MutableDenseMatrix

class GESolver:
    '''
    执行高斯消元法的求解器
    '''

    def __init__(self, mat: MutableDenseMatrix, evaluate = True) -> None:
        self.mat: MutableDenseMatrix = mat
        self.course: List[MutableDenseMatrix] = []

        self.evaluate = False
        if evaluate:
            self.get_course()
            self.evaluate = True

    def get_course(self) -> None:
        if not self.evaluate:
            self.reduce_row()

    def reduce_row(self) -> None:
        #Gauss消元
        mat: MutableDenseMatrix = self.mat.copy()
        for pivot_rowInd in range(mat.shape[0]): #最后一行不用选主元
            pivot = mat[pivot_rowInd, pivot_rowInd]
            #选主元，如果待消元的列不为0，则选为主元，否则选最开始一行的元素为主元
            if pivot == 0:
                for rowInd in range(pivot_rowInd+1, mat.shape[0]):
                    if mat[rowInd, pivot_rowInd] != 0:
                        mat = mat.elementary_row_op(op="n<->m", row1=pivot_rowInd, row2=rowInd)
                        self.course.append(mat.copy())
                        break
            #用主元所在的行消元
            for rowInd in range(pivot_rowInd+1, mat.shape[0]):
                if mat[rowInd, pivot_rowInd] != 0:
                    k = -sp.Mul(mat[rowInd, pivot_rowInd], sp.Pow(pivot, -1))
                    mat = mat.elementary_row_op(op='n->n+km', k=k, row1=rowInd, row2=pivot_rowInd)
                    self.course.append(mat.copy())

    def dict(self):

        # 返回该对象latex文本化的字典对象

        if not self.evaluate:
            self.get_course()
            
        js = {}

        js['course'] = []
        for m in self.course:
            js['course'].append(sp.latex(m))

        js['mat'] = sp.latex(self.mat)

        self.js = js
        return self.js
        
