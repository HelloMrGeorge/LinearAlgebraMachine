import sympy as sp
from sympy import S, Function, simplify, Symbol
from lam.determinant.mnmatrix import mn_matrix, scalar_mul

class id_func(Function):
    '''
    单位矩阵的内置函数
    '''
    @classmethod
    def eval(cls, x, y, m, n):
        if simplify(sp.Eq(x, y)) == True:
            return S.One
        elif simplify(sp.Eq(x, y)) == False:
            return S.Zero

class id_matrix(mn_matrix):
    '''
    定义单位矩阵
    '''
    def __init__(self) -> None:
        self.init_symbol()
        self.init_func(id_func)

class tridiagonal_func(Function):
    '''
    三对角矩阵的内置函数
    '''

    @classmethod
    def eval(cls, x, y, m, n, diag, diag2nd):
        if simplify(sp.Eq(x, y)) == True:
            return diag
        elif simplify(sp.Eq(sp.Abs(x-y), 1)) == True:
            return diag2nd
        elif simplify(sp.Gt(sp.Abs(x-y), 1)) == True:
            return S.Zero

class tridiagonal_matrix(mn_matrix):
    '''
    三对角矩阵的内置函数
    '''

    def __init__(self, diag, diag2nd) -> None:
        self.diag = simplify(diag)
        self.diag2nd = simplify(diag2nd)
        self.init_symbol()
        self.init_func()
    
    def init_func(self):
        self.func: Function = tridiagonal_func(self.x, self.y, self.m, self.n, self.diag, self.diag2nd)

class circ_func(Function):
    '''
    循环矩阵的内置函数
    '''
    @classmethod
    def eval(cls, x, y, m, n):
        if simplify(sp.Eq(x, y)) == True:
            return S.One
        elif simplify(sp.Eq(x, y)) == False:
            return S.Zero

if __name__ == "__main__":
    id = id_matrix()
    kid = scalar_mul(Symbol('c'),id)
    a = kid.get(kid.n,kid.n)
    print(a)