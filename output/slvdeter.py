from lam.determinant.course import det_course
from lam.readtext.readtext import readtext
import sympy as sp
import json
def slvdeter(a:str):
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
    json_str = json.dumps(course)
    print(json_str)
    with open('test_data.json', 'w') as json_file:
        json_file.write(json_str)
    return json_str



