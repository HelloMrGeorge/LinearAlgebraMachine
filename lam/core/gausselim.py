from lam.core import core

def gaussElim(mat):
    assert isinstance(mat,core.AlgArray)
    lis = [str(mat), ]

    for rowInd in range(mat.shape[0]-1):
        flag = False
        colInd = rowInd
        #判断第一列是否全为0，如果全为零则继续判断第二列，直到找道不为0的数
        for j in range(rowInd, mat.shape[1]):
            for i in range(rowInd, mat.shape[0]):
                if mat[i,j] != 0:
                    flag = True
                    mat.swapTran(i, rowInd)
                    lis.append(str(mat))
                    colInd = j
                    #记录不为的元素的所在列
                    break
            if flag:
                break

        #用rowInd行消元
        if flag:
            for i in range(rowInd+1, mat.shape[0]):
                k = -mat[i,colInd]/mat[rowInd,colInd]
                mat.plusTran(i, rowInd, k)
                lis.append(str(mat))
        else:
            continue

    return lis

if __name__ == '__main__':
    a = '1,3,4,1;2,3,4,1;3,4,5,1'
    b = core.interpret(a)
    c = gaussElim(b)
    for i in c:
        print(i)

