from lammatrix import *

def test1():
    id = id_matrix()
    kid = scalar_mul(Symbol('c'),id)
    a = kid.get(kid.n,kid.n)
    print(a)

def test2():
    tri = tridiagonal_matrix(1,2)
    ktri = scalar_mul(3, tri)
    res = ktri.get(tri.n,tri.n-1)
    print(res)

if __name__ == "__main__":
    test2()