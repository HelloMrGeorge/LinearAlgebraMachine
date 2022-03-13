import sympy as sp

def decompose_mono(matexpr) -> dict:
    '''
    把矩阵单项式拆分成系数和矩阵
    '''
    dic = {'coe':1, 'mat':0}
    if isinstance(matexpr, sp.MatrixBase):
        dic['mat'] = matexpr
        return dic
    else:
        for x in matexpr.args:
            if isinstance(x, sp.MatrixBase):
                dic['mat'] = x
            else:
                dic['coe'] = x
        return dic