import sympy as sp
from lam.determinant import course
from lam.printing import latextext

def formtest() -> str:
    mat = sp.Matrix([
        [1,2,3,4],
        [0,3,5,2],
        [9,8,7,3],
        [7,8,2,1],
    ])
    co = course.det_course(mat)
    text = ''
    for x in co['expand']:
        text = text + '$' + latextext.latex(x, mat_delim = '|') + '$' + r'<br>'
    for x in co['figure']:
        text = text + latextext.latex(x) + r'<br>'
    return text