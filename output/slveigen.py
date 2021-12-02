from lam.eigen.eigenvalue import *
import json
from lam.readtext.readtext import readtext
import sympy as sp
import sympy.core.numbers as nu
import numpy as np
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj,sp.core.numbers.Integer):
            return str(obj)
        else:
            return str(obj)
def getlambdamat(mat: sp.MutableDenseMatrix):#得到矩阵λE-A
    lambdamatrix = -mat
    lambdamatrix1 = sp.eye(mat.shape[0])
    x = sp.symbols("lambda")
    lambdamatrix1 = lambdamatrix1 * x
    lambdamatrix = lambdamatrix + lambdamatrix1
    return lambdamatrix
def getlambdamatvalue(mat: sp.MutableDenseMatrix):#得到列表[λ1E-A,λ2E-A,.....λiE-A]
    lambdamatrix = -mat
    lambdamatrix1 = sp.eye(mat.shape[0])
    eigenvalues=list(mat.eigenvals().keys())
    list0=[]
    for i in range(len(eigenvalues)):
        lambdamatrix2=lambdamatrix1*eigenvalues[i]
        lambdamatrix3 = lambdamatrix + lambdamatrix2
        list0.append(lambdamatrix3)
    return list0
def slveigengetcharpoly(a:str):#特征多项式
    eigenSolver = EigenSolver(readtext(a))
    p = eigenSolver.getCharpoly()
    p=sp.latex(p)
    json_str = json.dumps(p)
    return json_str
def slveigenvalue(a:str):#特征值
    eigenSolver = EigenSolver(readtext(a))
    p = eigenSolver.getEigenvalues()
    p = sp.latex(p)
    json_str = json.dumps(p)
    return json_str
def slveigenvectors(a:str):#特征向量
    eigenSolver = EigenSolver(readtext(a))
    eigenvectors = eigenSolver.getEigenvectors()
    eigenvectors_0 = []
    for i in range(len(eigenvectors)):
        p = []
        for j in range(len(eigenvectors[i][2])):
            p.append(sp.latex(eigenvectors[i][2][j]))
        m = [sp.latex(eigenvectors[i][0]), sp.latex(eigenvectors[i][1]), p]
        eigenvectors_0.append(m)
    eigenvectors=eigenvectors_0
    return eigenvectors
def slveigenCourse(a:str):#（特征值求解过程）
    eigenSolver=EigenSolver(readtext(a))
    p=eigenSolver.get_course()
    matrix=p['matrix']
    lambdamat = getlambdamat(matrix)
    lambdamatvalue = getlambdamatvalue(matrix)
    eigenvectors=p['eigenvectors']
    charpoly=p['charpoly']
    matrix=sp.latex(matrix)
    charpoly=sp.latex(charpoly)
    eigenvectors_0=[]
    for i in range(len(eigenvectors)):
        q = []
        for j in range(len(eigenvectors[i][2])):
            q.append(sp.latex(eigenvectors[i][2][j]))
        m = (sp.latex(eigenvectors[i][0]), sp.latex(eigenvectors[i][1]), q)
        eigenvectors_0.append(m)
    p['matrix']=matrix
    p['eigenvectors']=eigenvectors_0
    p['charpoly']=charpoly
    print(p['charpoly'])
    lambdamat = sp.latex(lambdamat)
    for i in range(len(lambdamatvalue)):
        lambdamatvalue[i] = sp.latex(lambdamatvalue[i])
    p.update({'lambdamat': lambdamat})
    p.update({'lambdamatvalue':lambdamatvalue})
    return p

if __name__ == '__main__':
    slveigenCourse("[[3,2,4],[2,0,2],[4,2,3]]")




