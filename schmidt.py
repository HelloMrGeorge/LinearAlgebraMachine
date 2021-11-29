from typing import Tuple
from sympy.matrices.dense import MutableDenseMatrix
from lam.core.solver import matSolver
from lam.metric.metricbase import inner

import sympy as sp
import logging
logging.basicConfig(level=logging.DEBUG)

class schmidtOrthogonalizer(matSolver):
    '''
    Schmidt正交化求解器
    '''
    def __init__(self, mat: MutableDenseMatrix) -> None:
        super().__init__(mat)
        self.dim: tuple = mat.shape
        self.vecs: MutableDenseMatrix = sp.zeros(*self.dim)
        self.inns: MutableDenseMatrix = sp.zeros(*self.dim)
        self.course: Tuple[MutableDenseMatrix, MutableDenseMatrix] = []

    def get_course(self, is_norm = False) -> Tuple[MutableDenseMatrix, MutableDenseMatrix]:
        self.course = self.schmidt()
        if is_norm:
            self.normalize()
        return (self.vecs, self.inns)

    @staticmethod
    def compute_epsilon(i: int, mat: MutableDenseMatrix, vecs: MutableDenseMatrix, inns: MutableDenseMatrix):
        epsilon = mat[i, :]
        for j in range(i):
            epsilon = epsilon - sp.Mul(sp.Rational(inns[i, j], inns[j, j])) * vecs[j, :]
        return epsilon
        

    def schmidt(self) -> Tuple[MutableDenseMatrix, MutableDenseMatrix]:
        vecs, inns = sp.zeros(*self.dim), sp.zeros(*self.dim) # vecs存储正交化后的向量，inns存储内积
        row_num = self.dim[0]
        mat = self.mat

        for i in range(row_num):
            for j in range(i):
                inns[i, j] = inner(mat[i,:], vecs[j,:])
            vecs[i, :] = self.compute_epsilon(i, self.mat, vecs, inns)
            inns[i, i] = inner(vecs[i, :], vecs[i, :])

        self.vecs, self.inns = vecs, inns
        return (vecs, inns)

    def normalize(self):
        # 归一化正交化后的向量
        for i in range(self.dim[0]):
            self.vecs[i, :] = self.vecs[i, :] / self.vecs[i, :].norm()



if __name__ == "__main__":
    mat = sp.Matrix([
        [1,1,0,0],
        [1,0,1,0],
        [-1,0,0,1],
        [1,-1,-1,1],
    ])
    solver = schmidtOrthogonalizer(mat)
    a = solver.get_course(is_norm=True)
    logging.debug(a)