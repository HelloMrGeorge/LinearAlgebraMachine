from lam.core import gelim, ndmatrix, output
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
    用Laplace定理对行列式的一行或一列展开

    Parameters: matrix: Algmat
                    待展开的矩阵
                m: int
                    展开行或列的序号，序号从零开始。
                axis： int
                    决定展开的轴，0表示按行展开，1表示按列展开
    Returns:    process: Step
                    返回单步计算的环节对象
    '''
    assert isinstance(matrix, ndmatrix.NumMatrix)
    mat = matrix.copy()
    step = output.MatAlgStep()
    for i in range(mat.shape[axis]):
        ind = [i,i]
        ind[axis] = m
        step.append({'operater': '+', 'coefficient': mat[ind[0],ind[1]], 'matrix': mat.copy().cofactorMat(ind[0], ind[1])})
    return step

def lapExpByStep(lastStep) -> output.Step:
    assert isinstance(lastStep, output.MatAlgStep)
    nextStep = output.MatAlgStep()
    for x in lastStep:
        t = laplaceExpand(x['matrix'], 0)
        for y in t:
            y['coeffcient'] = x['coeffcient'] * y['coeffcient']
        nextStep = nextStep + t
    return nextStep

def laplaceDet(process) -> None:
    '''
    三阶以上的行列式，返回展开后的过程的对象，三阶以内的行列式，返回数值。
    用于绘制Laplace展开过程的递归函数

    Parameters: matrix: Algmat
                    待求行列式的矩阵
    Returns:    process: Process
                    返回计算过程的过程对象
    '''
    assert isinstance(process, output.Process)
    # mat = matrix.copy()
    # if mat.shape[0] <= 3:
    #     step = output.AlgStep()
    #     step.append({'operater': '+', 'coefficient': det(mat)})
    #     process = output.Process()
    #     process.append(step)
    #     return process
    # else:
    #     process = laplaceExpand(mat)
    #     return process
    lastStep = process[-1]
    if isinstance(lastStep, output.AlgStep):
        val = 0
        for x in lastStep:
            val = val + x['coefficient']
        nextStep = output.AlgStep()
        nextStep.appendDic('+', val)
        process.append(nextStep)
    else:
        assert isinstance(lastStep, output.MatAlgStep)
        nextStep = lapExpByStep(lastStep)
        process.append(nextStep)
        laplaceDet(process)
    return
