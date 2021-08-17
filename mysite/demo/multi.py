import numpy as np

def strTomArr(mat):
    mat = mat.split(';')
    for x in range(len(mat)):
        mat[x] = mat[x].split(',')
        mat[x] = list(map(float,mat[x]))
    mat = np.array(mat)
    return mat

def inv(Mat):
    ans = strTomArr(Mat)
    ans = np.linalg.inv(ans)
    return ans

if __name__ == "__main__":
    a = '1,1,1;1,1,0;1,0,0'
    a = inv(a)
    print(a)