from numpy.lib import poly
from lam.core import expression, ndmatrix, output
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
    return mat

class Interpreter:
    '''
    解释器类，是创建矩阵，行列式等数据容器的工厂
    '''
    @staticmethod
    def __interpretAsNdmatrix(data: np.ndarray):
        arr = ndmatrix.NumMatrix(data.shape, dtype=float, buffer=data)
        return arr

    @staticmethod
    def __interpretAsDeterminant(data: np.ndarray):
        arr = det.Determinant(data.shape, dtype=float, buffer=data)
        return arr

    @classmethod
    def __interpretAsMonomial(cls, data: np.ndarray):
        mat = cls.__interpretAsNdmatrix(data)
        mono = expression.Monomial(mat)
        return mono

    @classmethod
    def __intepretAsPolymial(cls, data: np.ndarray):
        mono = cls.__interpretAsMonomial(data)
        poly = expression.Polynomial()
        poly.append(mono)
        return poly

    @classmethod
    def intepretAs(cls, name: str, data: str) -> output.htmlOutPut:
        typeDic = {
        'NumMatrix': cls.__interpretAsNdmatrix, 
        'Determinant': cls.__interpretAsDeterminant,
        'Monomial':cls.__interpretAsMonomial,
        'Polymial':cls.__intepretAsPolymial,
        }
        #解释器的主要函数
        arr = interpret(data)
        func = typeDic[name]
        arr = func(arr)
        return arr