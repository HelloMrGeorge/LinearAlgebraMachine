from lam.determinant.course import det_course
from lam.readtext.readtext import readtext
import sympy as sp
import json

def slvdeter(a:str):
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



