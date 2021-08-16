import numpy as np
from numpy.lib.function_base import percentile

class AlgArray(np.ndarray):

    def multTran(self, n, k):
        #初等变换1，非零的k乘第n行
        self[n] = k * self[n]
        return

    def plusTran(self, n, m, k):
        #初等变换2，把第m行的k倍加到第n行
        self[n] = k * self[m] + self[n]
        return

    def swapTran(self, n, m):
        #初等变换3，把m，n行交换
        t = self[m].copy()
        self[m] = self[n]
        self[n] = t
        return

def interpret(sMatrix):
    mat = sMatrix.split(';')
    for ind in range(len(mat)):
        mat[ind] = mat[ind].split(',')
        mat[ind] = list(map(float,mat[ind]))
    mat = np.array(mat, dtype=float)
    mat = AlgArray(mat.shape, dtype=float, buffer=mat)
    return mat

if __name__ == '__main__':
    a = '1,1,1;2,3,4;3,4,5'
    b = interpret(a)
    print(b)
    b.multTran(0, 3)
    print(b)
    b.plusTran(0, 1, 2)
    print(b)
    b.swapTran(0,1)
    print(b)