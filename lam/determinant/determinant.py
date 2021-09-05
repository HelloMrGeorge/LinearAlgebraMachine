import sympy as sp
from sympy.matrices import determinant
from lam.printing import latextext

class Determinant(sp.matrices.dense.MutableDenseMatrix, latextext.LatexText):
    '''
    创建行列式对象的类，基础sympy的MutableDenseMatrix，实现基本的行列式操作。
    在输出latex文本时，sympy未提供双竖线的行列式定界符，请在编辑网页文本时，自行修改，
    或使用printing子包的自定义latex模块，注意目前的子包并不支持递归。
    '''
    def latex(self) -> str:
        text = ''
        for i in range(self.shape[0]):
            text = text + ' & '.join(map(str, self[i, :])) + '\\\\'
        text = text[:-2]    #将最后一个换行符去掉
        text = '\\begin{vmatrix}' + text + '\\end{vmatrix}'
        return text

    def minor_subdet(self, i, j):
        #返回(i,j)元素的余子式，它只是表达式，没有经过计算
        mat =  self.minor_submatrix(i, j)
        return Determinant(mat)

    def cofactor_subdet(self, i, j):
        #返回(i,j)元素的代数余子式，它已将符号乘入矩阵中
        mat = self.minor_subdet(i, j)
        expr = sp.Mul((-1)**(i+j) ,mat)
        return expr