from lam.core import ndmatrix
from lam.det import det
import numpy as np
'''
处理输入数据的模块
'''
def interpret(matrix: str) -> np.ndarray:
    mat = matrix.split(';')
    for ind in range(len(mat)):
        mat[ind] = mat[ind].split(',')
        mat[ind] = list(map(float,mat[ind]))
    mat = np.array(mat, dtype=float)
    # mat = ndmatrix.NumMatrix(mat.shape, dtype=float, buffer=mat)
    return mat

class Interpreter:
    '''
    解释器类，是创建矩阵，行列式等数据容器的工厂
    '''
    @staticmethod
    def intepretAs(name: str, data: str):
        arr = interpret(data)
        if name == 'NumMatrix':
            arr = ndmatrix.NumMatrix(arr.shape, dtype=float, buffer=arr)
        elif name == 'Determinant':
            arr = det.Determinant(arr.shape, dtype=float, buffer=arr)
        return arr