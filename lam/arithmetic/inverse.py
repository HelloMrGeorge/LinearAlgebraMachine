from numpy import mat
import sympy as sp
from sympy.matrices.dense import Matrix, MutableDenseMatrix
from lam.determinant.determinant import is_singular

class MatrixInverse(sp.MutableDenseMatrix):

    def getInverseCourse(self) -> dict:

        course = {
            'matrix': sp.Matrix(self),
            'agumentedMatrix': self.getAgumentedMatrix(),
            'reduction': self.getReduction
        }
        return course

    def getAgumentedMatrix(self) -> Matrix:
        mat = sp.diag(*[1 for i in range(self.shape[0])])
        mat: Matrix = Matrix.hstack(self, mat)
        return mat

    def getReduction() -> list:
        reduct = []
        
        return reduct


if __name__ == "__main__":
    m = MatrixInverse([1,2,3,4])
    print(m, type(m))