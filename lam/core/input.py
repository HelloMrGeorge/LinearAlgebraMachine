from lam.core import ndmatrix
import numpy as np
'''
处理输出和输入数据的方法
'''
def interpret(matrix) -> ndmatrix.NumMatrix:
    mat = matrix.split(';')
    for ind in range(len(mat)):
        mat[ind] = mat[ind].split(',')
        mat[ind] = list(map(float,mat[ind]))
    mat = np.array(mat, dtype=float)
    mat = ndmatrix.NumMatrix(mat.shape, dtype=float, buffer=mat)
    return mat