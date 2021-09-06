from mpmath.functions.functions import arg
import sympy as sp
from sympy.matrices.expressions.matadd import MatAdd
from lam.determinant import cofactor

'''
实现Laplace展开的模块
有矩阵的表达式，请用MatAdd,MatMul实现加和乘
'''

def lap_expand(matrix, n: int = 0, axis: int = 0):
    #axis   0表示按行展开，否则按列展开
    expr = _lap_expr_0(matrix, n) if axis == 0 else _lap_expr_1(matrix, n)
    return expr

def _lap_expr_0(matrix, n: int = 0):
    #按行展开函数的实现
    expr, startInd = _lap_init_expr_0(matrix, n)
    for colInd in range(startInd+1 ,matrix.shape[1]):
        if matrix[n, colInd] in (0, 1, -1):
            t = sp.MatMul(matrix[n, colInd], cofactor.cofactor_submatrix(matrix, n, colInd), evaluate = True)
        else:
            t = sp.MatMul(matrix[n, colInd], cofactor.cofactor_submatrix(matrix, n, colInd), evaluate = False)
        if not isinstance(t, sp.matrices.expressions.special.ZeroMatrix):
            expr = sp.MatAdd(expr, t, evaluate = False)
    return expr
    
def _lap_init_expr_0(matrix, n: int = 0):
    #用于初始化按行展开的表达式
    expr = 0
    startInd = 0
    for colInd in range(matrix.shape[1]):
        if matrix[n, colInd] in (0, 1, -1): #去掉一些不必要的系数如，0，1，-1，使得输出格式化
            expr = sp.MatMul(matrix[n, colInd], cofactor.cofactor_submatrix(matrix, n, colInd), evaluate = True)
        else:
            expr = sp.MatMul(matrix[n, colInd], cofactor.cofactor_submatrix(matrix, n, colInd), evaluate = False)
        if not isinstance(expr, sp.matrices.expressions.special.ZeroMatrix):    #hint 0矩阵不等于0，不能用==判别
            startInd = colInd
            break
    return (expr, startInd)

def _lap_expr_1(matrix, n: int = 0):
    expr, startInd = _lap_init_expr_1(matrix, n)
    for rowInd in range(startInd+1 ,matrix.shape[0]):
        if matrix[rowInd, n] in (0, 1, -1):
            t = sp.MatMul(matrix[rowInd, n], cofactor.cofactor_submatrix(matrix, rowInd, n), evaluate = True)
        else:
            t = sp.MatMul(matrix[rowInd, n], cofactor.cofactor_submatrix(matrix, rowInd, n), evaluate = False)
        if not isinstance(t, sp.matrices.expressions.special.ZeroMatrix):
            expr = sp.MatAdd(expr, t, evaluate = False)
    return expr

def _lap_init_expr_1(matrix, n: int = 0):
    expr = 0
    startInd = 0
    for rowInd in range(matrix.shape[1]):
        if matrix[rowInd, n] in (0, 1, -1): #去掉一些不必要的系数如，0，1，-1
            expr = sp.MatMul(matrix[rowInd, n], cofactor.cofactor_submatrix(matrix, rowInd, n), evaluate = True)
        else:
            expr = sp.MatMul(matrix[rowInd, n], cofactor.cofactor_submatrix(matrix, rowInd, n), evaluate = False)
        if not isinstance(expr, sp.matrices.expressions.special.ZeroMatrix):    #hint 0矩阵不等于0，不能用==判别
            startInd = rowInd
            break
    return (expr, startInd)

def lap_exp_coe(expr, n: int = 0, axis: int = 0):  
    '''
    带系数的Laplace展开
    expr    是系数乘矩阵的一个单项式
    '''
    if isinstance(expr, sp.MatrixBase):
        # print(type(expr))
        return lap_expand(expr, n, axis)

    coe = 1
    for x in expr.args:
        if isinstance(x, sp.MatrixBase):
            expr = lap_expand(x, n, axis)
        else:
            coe = x
    if coe in (0, 1, -1):
        expr = sp.MatMul(coe, expr, evaluate = True)
    else:
        expr = sp.MatMul(coe, expr, evaluate = False)
    return expr

def lapexp_expr(expr):
    '''
    输入为表达式的Laplace展开函数
    expr: MatrixBaser/Expr
    '''
    if isinstance(expr, sp.MatrixBase):
        return lap_expand(expr)
    args = []
    read_mat_mono(args, expr)
    expr_list = [0 for i in range(len(args))]
    for i in range(len(args)):
        expr_list[i] = lap_exp_coe(args[i])
    expr = sp.MatAdd(*expr_list)
    return expr

def read_mat_mono(args: list, poly: sp.Expr):
    #读取矩阵多项式的单项式
    for x in poly.args:
        if isinstance(x, MatAdd):
            read_mat_mono(args, x)
        else:
            args.append(x)
    
