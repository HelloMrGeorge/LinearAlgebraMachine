from sympy import *
from sympy.matrices import matrices

class MatrixReduction():
    '''
    带步骤输出的矩阵消元类
    '''
    def __init__(self, matrix: MatrixBase) -> None:
        self.matrix = matrix
        self.course = [matrix.copy(), ]
        return

    def echelon_form(self) -> list:
        for rowInd in range(self.matrix.shape[0]-1):
            self.__reduce_col(rowInd)
        return self.course

    def __reduce_col(self, n: int) -> None:
        row = self.matrix[n, :]
        pivotInd = self.__pivot_Ind(row)
        for rowInd in range(n+1, self.matrix.shape[0]):
            if pivotInd > self.__pivot_Ind(self.matrix[rowInd, :]):
                self.matrix = self.matrix.elementary_row_op('n<->m', n, rowInd)
                self.course.append(self.matrix.copy())
        for rowInd in range(n+1, self.matrix.shape[0]):
            if self.matrix[rowInd, pivotInd] != 0:
                k = Rational(-self.matrix[rowInd, pivotInd],row[pivotInd])
                self.matrix = self.matrix.elementary_row_op('n->n+km', rowInd, k, n)
                self.course.append(self.matrix.copy())
        return

    def __pivot_Ind(self, col: MatrixBase) -> int:
        for colInd in range(col.shape[1]):
            if col[colInd] != 0:
                return colInd
        return col.shape[1]