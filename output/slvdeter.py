from lam.determinant.course import det_course
from lam.readtext.readtext import readtext
import numpy as np
from lam.eigen.eigenvalue import *
import json
from math import sqrt
class MyEncoder(json.JSONEncoder):#重新定义的MyEncoder函数
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)

def slvdeter(a:str):
    #将str格式改为json格式并写入文件test_data.json（行列式模块）
    course = det_course(readtext(a))
    expand = course["expand"]
    figure = course["figure"]
    expand = list(map(sp.latex, expand))
    figure = list(map(sp.latex, figure))
    course["expand"] = expand
    course["figure"] = figure
    json_str = json.dumps(course)
    with open('test_data.json', 'w') as json_file:
        json_file.write(json_str)
    return json_str
    
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


