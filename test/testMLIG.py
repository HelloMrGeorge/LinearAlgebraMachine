import sympy as sp
from lam.linspace.MLIG import MLIGSolver


if __name__ == "__main__":
    A = [[1,2,3,-1], [3,2,1,-1], [2,3,1,1], [2,2,2,-1], [5,5,2,0]]
    for i in range(len(A)):
        A[i] = sp.Matrix(A[i])
    solver = MLIGSolver(A)
    co: MLIGSolver = solver.get_course()
    print(co.coefs)
    print(co.MLIG)
    print(co.position)