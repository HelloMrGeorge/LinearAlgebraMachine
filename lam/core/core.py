import numpy as np
from numpy.matrixlib import mat

class Algmat(np.ndarray):
#初等变换部分
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

#行列式部分       
    def cofactorMat(self,m,n):
        #求(m,n)元的余子矩阵，注意开头是序号0
        mat = np.delete(self,m,0)
        mat = np.delete(mat,n,1)
        return mat

class Step:
#一般环节对象

    def __init__(self):
        self.matList = []
        self.coeList = []
        return
    
    def __str__(self):
        return str(list(map(str, self.matList)))

    def print(self):
        for i in self.matList:
            print(i)
        return

class Process:
#过程对象，用于储存环节
    
    def __init__(self, step):
        assert isinstance(step, Step)
        self.stepList = [step, ]

    def print(self):
        for i in self.stepList:
            i.print()
        return