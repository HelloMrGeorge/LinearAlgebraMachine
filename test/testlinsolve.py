from sympy import symbols, Matrix, linsolve
import sympy

w, x, y, z = symbols("w,x,y,z")

def test1(): # 线性方程有唯一解
    
    A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
    b = Matrix([3, 6, 9])
    res = linsolve((A, b), [x, y, z])
    for i in res.args[0]:
        print(i.subs(z, 0))

def test2(): #线性方程有多解
    
    A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = Matrix([3, 6, 9])
    res = linsolve((A, b), x, y, z)
    for i in res.args[0]:
        print(i.subs(z, 0))

def test3(): #线性方程无解
    
    A = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    b = Matrix([3, 6, 9])
    res = linsolve((A, b), x, y, z)
    print(res,isinstance(res, sympy.sets.sets.EmptySet))

def test4():

    A = Matrix([[1, 2, 3, 2], [4, 5, 6, 3], [7, 8, 9, 3]])
    b = Matrix([3, 6, 9])
    res = linsolve((A, b), w, x, y, z)
    print(A)
    print(b)
    print(res)

if __name__ == "__main__":
    test4()
