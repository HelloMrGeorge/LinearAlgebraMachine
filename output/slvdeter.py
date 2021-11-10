from lam.determinant.course import det_course
from lam.readtext.readtext import readtext
import sympy as sp
import json
def slvdeter(a:str):
    M=det_course(readtext(a))
    process=M["expand"]
    result=M["figure"]
    m=sp.latex(process)
    n=sp.latex(result)
    course = {}
    course['expand'] = m
    course['figure'] = n
    json_str = json.dumps(course)
    with open('test_data.json', 'w') as json_file:
        json_file.write(json_str)
    return json_str


