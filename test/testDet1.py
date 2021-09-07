import __init__
import sympy as sp

from lam.linearequation import reduction, solve, outtext
from lam.determinant import determinant, laplaceexpand, course
from lam.printing import latextext

a = sp.Matrix([
    [1,2,10,20,30,2],
    [1,2,0,8,0,4],
    [1,2,3,0,0,5],
    [0,7,0,1,0,3],
    [0,0,0,0,3,2],
    [1,2,4,5,6,2],
])

co = course.det_course(a)

for i in co['expand']:
    print('展开：' + str(i))
for i in co['figure']:
    print('计算' + str(i))
print(a.det())
