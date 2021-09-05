from sympy import *
from sympy.matrices import matrices

class MatrixReduction():
    '''
    带步骤输出的矩阵消元类
    '''
    def __init__(self, matrix: MatrixBase) -> None:
        '''
        Parameter
            matrix  待消元的矩阵
        '''
        self.matrix = matrix
        self.course = [matrix.copy(), ]
        return

    def echelon_form(self) -> list:
        '''
        化矩阵为阶梯形，返回一个列表，存有每次初等变换后的矩阵
        '''
        if not self.matrix.is_echelon:
            for rowInd in range(self.matrix.shape[0]-1):
                self.__reduce_col(rowInd)
        return

    def __reduce_col(self, n: int) -> None:
        #用于逐行消元，n是用于消去后面行元素的行
        row = self.matrix[n, :]
        pivotInd = self.pivot_Ind(row)
        for rowInd in range(n+1, self.matrix.shape[0]):
            if pivotInd > self.pivot_Ind(self.matrix[rowInd, :]):
                self.matrix = self.matrix.elementary_row_op('n<->m', n, rowInd) #交换行，使得长的行放在最上面
                self.course.append(self.matrix.copy())
        pivotInd = self.pivot_Ind(self.matrix[n, :])    #因为可能交换行，所以重置了主元
        for rowInd in range(n+1, self.matrix.shape[0]):
            if self.matrix[rowInd, pivotInd] != 0:
                k = Rational(-self.matrix[rowInd, pivotInd],self.matrix[n, pivotInd])
                self.matrix = self.matrix.elementary_row_op('n->n+km', rowInd, k, n)    #用第n行消去后面的行
                
        return  self.course.append(self.matrix.copy())

    def pivot_Ind(self, row: MatrixBase) -> int:
        #找主元，主元是每行元素中从左到右第一个不为0的元素
        for colInd in range(row.shape[1]):
            if row[colInd] != 0:
                return colInd
        return row.shape[1] #如果一行全为0，主元序号设置为最大索引+1