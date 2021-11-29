import sympy as sp
from sympy import MutableDenseMatrix

import logging
logging.basicConfig(level=logging.DEBUG)

def inner(a: MutableDenseMatrix, b: MutableDenseMatrix) -> MutableDenseMatrix:
    # 封装内积
    return a.dot(b)

def normalize(vec: MutableDenseMatrix):
    # 单位化向量
    return vec / vec.norm()

if __name__ == '__main__':
    a = sp.Matrix([1,2,3])
    b = sp.Matrix([5,32,4])
    logging.debug(inner(a, b))