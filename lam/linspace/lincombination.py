import copy
import sympy as sp
from sympy import MutableDenseMatrix, symbols
from sympy.abc import w, x, y, z
from typing import List



def __is_matrix_lincombination(group: List, vect: MutableDenseMatrix, coef: list = []) -> bool:
    '''
    判断vect是否是group的线性组合，专用于数字向量。
    '''
    num = len(group)

    group = copy.deepcopy(group) #重新把列表group构造成矩阵
    for i in range(len(group)):
        group[i] = list(group[i])
    group = sp.Matrix(group).T 
    
    flag = False
    vars = [] # 创建未知元，用以求解方程
    for i in range(num):
        vars.append(symbols(f"x{i}"))
    res = sp.linsolve((group, vect), vars)

    if isinstance(res, sp.sets.sets.EmptySet):
        return flag
    else:
        flag = True
        for x in res.args[0]: #res是有限集，其参数可以被迭代器调用
            for i in range(num):
                x = x.subs(vars[i], 0)
            coef.append(x)
        return flag
        

def is_lincombination(group: List, vect, coef: list = []) -> bool:
    '''
    判断vect是否是group的线性组合，coef作为引用参数用于返回线性组合的系数
    '''
    flag = False
    if isinstance(vect, MutableDenseMatrix):
        flag = __is_matrix_lincombination(group, vect, coef)
    return flag


if __name__ == "__main__":
    A = [[1,2,3,-1], [3,2,1,-1], [2,3,1,1], [2,2,2,-1]]
    b = sp.Matrix([5,5,2,0])
    for i in range(len(A)):
        A[i] = sp.Matrix(A[i])
    coef = []
    is_lincombination(A, b, coef)
    print(coef)