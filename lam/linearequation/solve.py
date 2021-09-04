from sympy import *
from lam.linearequation import reduction

class EquationSolve(reduction.MatrixReduction):

    def __init__(self, matrix: MatrixBase) -> None:
        super.__init__(matrix)
        return
    
    def Solution(self) -> list:
        
        return self.course
        

