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
    print(eigenvectors[0][2])
    for i in range(len(eigenvectors)):
        p = []
        for j in range(len(eigenvectors[i][2])):
            p.append(sp.latex(eigenvectors[i][2][j]))
        m = [sp.latex(eigenvectors[i][0]), sp.latex(eigenvectors[i][1]), sp.latex(p)]
        eigenvectors_0.append(m)
    eigenvectors=eigenvectors_0
    json_str = json.dumps(eigenvectors)
    return json_str
def slveigenCourse(a:str):#（特征值求解过程）
    eigenSolver=EigenSolver(readtext(a))
    p=eigenSolver.get_course()
    matrix=p['matrix']
    eigenvectors=p['eigenvectors']
    charpoly=p['charpoly']
    lambdamat=p['lambdamat']
    lambdamat=sp.latex(lambdamat)
    lambdamatvalue=p['lambdamatvalue']
    for i in range(len(lambdamatvalue)):
        lambdamatvalue[i]=sp.latex(lambdamatvalue[i])
    matrix=sp.latex(matrix)
    charpoly=sp.latex(charpoly)
    eigenvectors_0=[]
    for i in range(len(eigenvectors)):
        q = []
        for j in range(len(eigenvectors[i][2])):
            q.append(sp.latex(eigenvectors[i][2][j]))
        m = (sp.latex(eigenvectors[i][0]), sp.latex(eigenvectors[i][1]), sp.latex(q))
        eigenvectors_0.append(m)
    p['lambdamat']=lambdamat
    p['matrix']=matrix
    p['eigenvetors']=eigenvectors_0
    p['lambdamatvalue']=lambdamatvalue
    p['charpoly']=charpoly
    json_str = json.dumps(p,cls=MyEncoder,indent=4)
    return json_str

slveigenCourse("[[1,2,3],[5,62,2],[245,4,6]]")
