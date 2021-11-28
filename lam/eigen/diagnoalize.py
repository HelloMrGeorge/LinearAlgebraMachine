from lam.eigen.eigenvalue import EigenSolver
import sympy as sp

import logging
logging.basicConfig(level=logging.WARN)

class Diagnoalizer(EigenSolver):
    
    def diagnoalize(self):
        return self.mat.diagonalize()

if __name__ == "__main__":
    mat = [
        [1,1,3],
        [1,1,1],
        [3,1,1],
    ]
    mat = sp.Matrix(mat)
    solver = Diagnoalizer(mat)
    diag = solver.diagnoalize()
    logging.info(diag)
    vect = solver.getEigenvectors()
    logging.info(vect)
