import sympy as sp
from lam.linearequation import reduction, solve


def output_text(course: list) -> str:
    text = ''
    for x in course:
        text = text + f'${sp.latex(x)}$<br>'
    return text

def main():
    a = sp.Matrix([
        [0,0,18,6],
        [1,3,2,3],
        [0,0,3,1],
    ])
    co = solve.EquationSolve(a)
    co = co.get_course()
    return output_text(co)
