import sympy as sp

def cofactor_submatrix(mat, i, j):
    #返回(i,j)元素的代数余子式，它已将符号乘入矩阵中
    mat = mat.minor_submatrix(i, j)
    expr = sp.Mul((-1)**(i+j) ,mat)
    return expr