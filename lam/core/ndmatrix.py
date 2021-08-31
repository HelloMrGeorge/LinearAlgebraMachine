import numpy as np
from lam.core import output

class NumMatrix(np.ndarray, output.htmlOutPut):
    '''
    数值矩阵类，定义存储元素为数值类型的矩阵容器。
    下面定义了三种初等变换，求余子矩阵，网页输出等方法。
    '''
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

#输出latex格式的矩阵
    def htmlStr(self):
        text = ''
        for i in range(self.shape[0]):
            text = text + '&'.join(map(str, self[i])) + '\\\\'
        text = '$\\begin{bmatrix}' + text + '\\end{bmatrix}$'
        return text