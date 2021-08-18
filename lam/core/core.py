import numpy as np

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

#输出latex格式的矩阵
    def htmlStr(self):
        content = ''
        for i in range(self.shape[0]):
            content = content + '&'.join(map(str, self[i])) + '\\\\'
        htmlS = '$\\begin{bmatrix}' + content + '\\end{bmatrix}$'
        return htmlS


class Step:
#一般环节对象

    def __init__(self):
        self.matList = []
        return
    
    def __str__(self):
        content = ''
        for i in self.matList:
            content = content + i.htmlStr()
        return content

    def print(self):
        for i in self.matList:
            print(i)
        return

class Process:
#过程对象，用于储存环节
    
    def __init__(self, step):
        assert isinstance(step, Step)
        self.stepList = [step, ]

    def __str__(self):
        content = ''
        for i in self.stepList:
            content = content + str(i)
        return content

    def print(self):
        for i in self.stepList:
            i.print()
        return

class LapStep(Step):
#拉普拉斯展开过程对象
    def __init__(self):
        super(self).__init__()
        self.ceoList = []
        return
    
    def __str__(self):
        self.matList = np.array(self.matList)
        return str(self.matList)
