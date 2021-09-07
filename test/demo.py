import sympy as sp
from lam.linearequation import reduction, solve, outtext
from lam.determinant import determinant, laplaceexpand, course
from lam.printing import latextext
s1 = sp.symbols('s1')
# a = sp.Matrix([
#     [-1,3,1,0,3],
#     [1,2,5,8,23],
#     [3,2,-4,0,8],
#     [8,9,5,1,2],
#     [1,-7,6,5,3]
# ])
a = sp.Matrix([
    [1,2,0,0,0],
    [1,2,0,0,0],
    [1,2,3,0,0],
    [0,0,0,1,0],
    [0,0,0,0,3]
])
# a = determinant.Deter(a)
# b = laplaceexpand.lapexp_expr(a)
# b = laplaceexpand.lapexp_expr(b)
# b = laplaceexpand.lapexp_expr(b)
co = course.det_course(a)

for i in co['expand']:
    print('展开：' + str(i))
for i in co['figure']:
    print('计算' + str(i))
print(a.det())
