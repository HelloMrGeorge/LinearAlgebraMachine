from lam.core import gausselim, ndmatrix
import numpy
'''
det.py
    实现计算行列式等相关功能
'''
def det(mat):
    #直接调用numpy求行列式的值
    return numpy.linalg.det(mat)

def laplaceExpand(matrix, m, axis=0):
    '''
    单步Laplace定理展开行列式

    Parameters: matrix: Algmat
                    待展开的矩阵
                m: int
                    展开行或列的序号，序号从零开始。
                axis： int
                    决定展开的轴，0表示按行展开，1表示按列展开
    Returns:    process: Process
                    返回单步计算的过程对象
    '''
    assert isinstance(matrix, ndmatrix.Algmat)
    mat = matrix.copy()
    step = ndmatrix.LapStep()
    for i in range(mat.shape[axis]):
        ind = [i,i]
        ind[axis] = m
        step.matList.append(mat.cofactorMat(ind[0],ind[1]))
        step.coeList.append(mat[ind])

    return ndmatrix.Process(step)

def laplaceDet(matrix):
    '''
    方法仍在建设中
    用Laplace定理展开行列式至三阶，然后求值

    Parameters: matrix: Algmat
                    待求行列式的矩阵
    Returns:    process: Process
                    返回计算过程的过程对象
    '''
    assert isinstance(matrix, ndmatrix.Algmat)
    mat = matrix.copy()
    if mat.shape[0] <= 3:
        pass
    return