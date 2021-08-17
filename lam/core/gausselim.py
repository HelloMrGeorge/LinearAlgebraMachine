from lam.core import core

def gaussElim(matrix):
    assert isinstance(matrix,core.Algmat)
    mat = matrix.copy()
    t = core.Step()
    t.matList.append(mat.copy())
    process = core.Process(t)

    for rowInd in range(mat.shape[0]-1):
        flag = False
        colInd = rowInd
        #判断第一列是否全为0，如果全为零则继续判断第二列，直到找道不为0的数
        for j in range(rowInd, mat.shape[1]):
            for i in range(rowInd, mat.shape[0]):
                if mat[i,j] != 0:
                    flag = True
                    t = mat.copy()
                    mat.swapTran(i, rowInd)
                    if not (t == mat).all():
                        #经过变换后，没有变化则不计入结果
                        t = core.Step()
                        t.matList.append(mat.copy())
                        process.stepList.append(t)
                    colInd = j
                    #记录不为0的元素的所在列
                    break
            if flag:
                break

        #用rowInd行消元
        if flag:
            for i in range(rowInd+1, mat.shape[0]):
                k = -mat[i,colInd]/mat[rowInd,colInd]
                t = mat.copy()
                mat.plusTran(i, rowInd, k)
                if not (t == mat).all():
                    t = core.Step()
                    t.matList.append(mat.copy())
                    process.stepList.append(t)
        else:
            continue

    return process



