from lam.determinant.course import det_course
from lam.readtext.readtext import readtext
import numpy as np
import sympy as sp
import json
from math import sqrt
def slvdeter(a:str):#将str格式改为json格式并写入文件test_data.json（行列式模块）
    M=det_course(readtext(a))
    expand=M["expand"]
    figure=M["figure"]
    expand=list(map(sp.latex,expand))
    figure=list(map(sp.latex,figure))
    course = {}
    course['expand'] = expand
    course['figure'] = figure
    json_str = json.dumps(course)
    with open('test_data.json', 'w') as json_file:
        json_file.write(json_str)
    return json_str




