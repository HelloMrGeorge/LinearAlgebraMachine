import sympy as sp
from sympy.matrices.expressions.matadd import MatAdd

from lam.determinant import laplaceexpand
from lam.core.matrixexpression import decompose_mono


def det_course(matrix: sp.MatrixBase):
    course = {}
    course['expand'] = lap_expand_course(matrix)
    expr = course['expand'][-1]
    course['figure'] = detpoly_figure_course(expr)
    return course

def lap_expand_course(matrix: sp.MatrixBase):
    time = matrix.shape[0] - 3  #三阶以内不展开
    expr = matrix
    course = [0 for i in range(time + 1)]
    course[0] = matrix
    for i in range(time):
        expr = laplaceexpand.lapexp_expr(expr)
        course[i+1] = expr
    return course

def detpoly_figure_course(expr: MatAdd):
    course = []
    expr_list = []
    laplaceexpand.read_mat_mono(expr_list, expr)
    for ind in range(len(expr_list)):
        dic = decompose_mono(expr_list[ind])
        expr_list[ind] = sp.Mul(dic['coe'], dic['mat'].det())
    course.append(sp.Add(*expr_list, evaluate = False))
    course.append(course[-1].doit())
    return course
