import sympy as sp
from sympy import MutableDenseMatrix, Symbol, latex
from lam.core.solver import CoreSolver

class PolySolver(CoreSolver):
    '''
    计算矩阵多项式的值
    '''
    def __init__(self, mat: MutableDenseMatrix, var: Symbol, expr: sp.Expr, evaluate=True) -> None:
        self.mat: MutableDenseMatrix = mat # 矩阵的值
        self.var: Symbol = var # 定义主变量
        self.poly: sp.Poly = sp.Poly(sp.simplify(expr), var) # 关于矩阵的标量型多项式，注意必须用一次simplify，否则可能表达式会被视为一个整体

        self.matPoly: sp.MatrixExpr = None # 关于矩阵的矩阵型多项式
        self.subPoly: sp.MatrixExpr= None # 代入矩阵值的多项式
        self.result: MutableDenseMatrix = None # 矩阵多项式的值
        super().__init__(evaluate)

    def toExecute(self) -> None:
        coef = self.poly.all_coeffs()
        matVar = sp.MatrixSymbol('A', self.mat.shape[0], self.mat.shape[1])
        self.matPoly = (sp.Matrix(coef).T @ sp.Matrix([sp.MatPow(matVar, i) for i in range(len(coef)-1, -1, -1)]))[0]
        self.subPoly = self.matPoly.subs(matVar, self.mat)
        self.result = self.subPoly.as_explicit()

    def toDict(self) -> dict:
        js = {}
        js['mat'] = latex(self.mat)
        js['result'] = latex(self.result)
        js['matPoly'] = latex(self.matPoly)
        js['subPoly'] = latex(self.subPoly)
        return js
