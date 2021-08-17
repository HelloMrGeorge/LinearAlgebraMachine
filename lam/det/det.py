from lam.core import gausselim, core
import numpy

def det(mat):
    #直接调用numpy求行列式的值
    return numpy.linalg.det(mat)

def laplaceExpand(matrix, m, axis=0):
    '''
    用Laplace定理展开行列式

    Parameters: matrix: Algmat
                    待展开的矩阵
                m: int
                    展开行或列的序号，序号从零开始。
                axis： int
                    决定展开的轴，0表示按行展开，1表示按列展开
    Returns:    process: Process
                    返回过程对象
    '''
    assert isinstance(matrix, core.Algmat)
    mat = matrix.copy()
    step = core.Step()
    for i in range(mat.shape[axis]):
        ind = [i,i]
        ind[axis] = m
        step.matList.append(mat.cofactorMat(ind[0],ind[1]))
        step.coeList.append(mat[ind])

    return core.Process(step)