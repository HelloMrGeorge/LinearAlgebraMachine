from lam.core import ndmatrix, output, expression
import numpy as np
'''
实现计算行列式等相关功能
'''
class Determinant(ndmatrix.NumMatrix, output.htmlOutPut):

    def htmlStr(self):
        text = ''
        for i in range(self.shape[0]):
            text = text + '&'.join(map(str, self[i])) + '\\\\'
        text = '$\\begin{vmatrix}' + text + '\\end{vmatrix}$'
        return text

    #求(m,n)元的余子式，注意开头是序号0       
    def cofactor(self,m,n):  
        mat = np.delete(self,m,0)
        mat = np.delete(mat,n,1)
        return mat


def det(mat):
    #直接调用numpy求行列式的值
    return np.linalg.det(mat)


def laplaceExpand(matrix: Determinant, m: int = 1, coefficient  = 1, axis=0) -> expression.Polynomial:
    '''
    单步Laplace定理展开行列式

    Parameters: matrix: Determinant
                    待展开的矩阵
                m: int
                    展开行或列的序号，序号从零开始。
                coeffient:  float
                    矩阵前的系数
                axis： int
                    决定展开的轴，0表示按行展开，1表示按列展开
    Returns:    expr: expression.Polynomial
                    返回计算结果的多项式对象
    '''
    mat = matrix.copy()
    expr = expression.Polynomial()
    for i in range(mat.shape[axis]):
        ind = [i,i]
        ind[axis] = m
        mono = expression.Monomial(mat.cofactor(ind[0], ind[1]), coefficient*mat[ind[0], ind[1]])
        expr.append(mono)
    return expr

def LEofMono(mono: expression.Monomial):
    '''
    输入为单项式的拉普拉斯展开
    '''
    #检查是否大于3阶，否则直接求解
    if mono.element.shape[0] > 3:
        expr = laplaceExpand(mono.element, 0, mono.coefficient)
        return expr
    else:
        t = expression.Monomial(det(mono.element)*mono.coefficient)
        expr = expression.Polynomial()
        expr.append(t)
        return expr

def LEbyStep(poly: expression.Polynomial):
    '''
    输入为多项式的拉普拉斯展开，每个多项式都算解行列式的一个环节
    '''
    expr = expression.Polynomial()
    #检查多项式的元素是矩阵还是数值，矩阵则继续展开，数值则直接求和
    if isinstance(poly[0].element, ndmatrix.NumMatrix):
        for mono in poly:
            expr.extend(LEofMono(mono))
    elif len(poly) > 1:
        sum = 0
        for mono in poly:
           sum = mono.element + sum
        expr.append(expression.Monomial(sum)) 
    else:
        expr = None
    return expr


class LEIterator():
    '''
    用Laplace展开解行列式的迭代器
    '''
    def __init__(self, poly: expression.Polynomial) -> None:
        self.poly = poly
        return
    
    def __iter__(self):
        return self

    def __next__(self): 
        t = LEbyStep(self.poly) #先存一个临时变量，防止赋值为None
        if isinstance(t, expression.Polynomial):
            self.poly = t
            return self.poly
        else:
            raise StopIteration

