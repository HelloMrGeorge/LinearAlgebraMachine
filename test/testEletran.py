from lam.determinant.eletran import *
from lam.determinant.lammatrix import *

def test1():
    mat: mn_matrix = circ_matrix()
    mat = ele_col_tran_kmn(mat, 2, 2, mat.n)
    res = mat.get(mat.n, mat.n)
    print(res)


if __name__ == "__main__":
    test1()