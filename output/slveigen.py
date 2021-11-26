from lam.eigen.eigenvalue import *
import json
from lam.readtext.readtext import readtext
def slvdeter_eigen(a:str):#（特征值模块）
    eigenSolver=EigenSolver(readtext(a))
    p=eigenSolver.getEigenvectorsCourse()
    matrix=p['matrix']
    eigenvectors=p['eigenvectors']
    charpoly=p['charpoly']
    matrix=sp.latex(matrix)
    charpoly=sp.latex(charpoly)
    for m in eigenvectors:
        m=sp.latex(m)
    p['matrix']=sp.latex(matrix)
    p['eigenvetors']=sp.latex(eigenvectors)
    p['charpoly']=sp.latex(charpoly)
    p=sp.latex(p)
    json_str = json.dumps(p)
    return json_str
