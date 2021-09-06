import sympy as sp

class Deter(sp.matrices.dense.MutableDenseMatrix):
    '''
    Deter   创建行列式对象的类，没有写全名Determinant是因为会和sympy的某些类冲突
    继承sympy的MutableDenseMatrix，实现基本的行列式操作。
    在输出latex文本时，sympy未提供双竖线的行列式定界符，请在编辑网页文本时，自行修改，
    或使用printing子包的自定义latex模块。
    在打印latex文本时请使用关键字参数mat_delim = '|'，以实现双竖线输出。
    '''

    def cofactor_subdet(self, i, j):
        #返回(i,j)元素的代数余子式，它已将符号乘入矩阵中
        mat = self.minor_submatrix(i, j)
        expr = sp.Mul((-1)**(i+j) ,mat)
        return expr



        