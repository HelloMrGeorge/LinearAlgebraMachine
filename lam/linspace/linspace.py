import sympy as sp
from lam.core.solver import CoreSolver
from lam.linequ.gausslimination import GESolver 

class LinDependenceSolver(CoreSolver):
    '''
    判断向量组是否线性相关
    '''
    def __init__(self, mat: sp.MutableDenseMatrix, evaluate=True) -> None:
        self.mat: sp.MutableDenseMatrix = mat
        self.GES: GESolver = None
        self.result: bool = False
        super().__init__(evaluate)

    def toExecute(self) -> None:
        self.GES = GESolver(self.mat)
        if self.GES.course[-1][-1, -1] != 0:
            self.result = True

    def toDict(self) -> dict:
        js = {}
        js['mat'] = sp.latex(self.mat)
        js['GES'] = self.GES.dict()
        js['result'] = self.result
        return js