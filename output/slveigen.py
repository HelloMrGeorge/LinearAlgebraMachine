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
def slvdeter_eigen(a:str):#（特征值模块）
    eigenSolver=EigenSolver(readtext(a))
    p=eigenSolver.getEigenvectorsCourse()
    matrix=p['matrix']
    eigenvectors=p['eigenvectors']
    charpoly=p['charpoly']
    matrix=sp.latex(matrix)
    charpoly=sp.latex(charpoly)
    eigenvectors_0=[]
    for i in range(len(eigenvectors)):
        m = (sp.latex(eigenvectors[i][0]),sp.latex(eigenvectors[i][1]),sp.latex(eigenvectors[i][2][0]))
        eigenvectors_0.append(m)
    p['matrix']=matrix
    p['eigenvetors']=eigenvectors_0
    p['charpoly']=charpoly
    json_str = json.dumps(p,cls=MyEncoder,indent=4)
    return json_str

