from lam.determinant.course import det_course
from lam.readtext.readtext import readtext
import numpy as np

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

def slvdeter(a:str):#将str格式改为json格式并写入文件test_data.json（行列式模块）
    M=det_course(readtext(a))
    process=M["expand"]
    result=M["figure"]
    for m in process:
        m=sp.latex(m)
    for n in result:
        n=sp.latex(n)
    course = {}
    course['expand'] = sp.latex(process)
    course['figure'] = sp.latex(result)
    print(course)
    json_str = json.dumps(course)
    print(json_str)
    with open('test_data.json', 'w') as json_file:
        json_file.write(json_str)
    return json_str


