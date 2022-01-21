from eletran import *
from lam.determinant.lammatrix import *

def test1():
    mat: mn_matrix = circ_matrix()
    mat = ele_row_tran_mn(mat, 2, mat.n)
    res = mat.get(2, mat.n)
    print(res)


if __name__ == "__main__":
    test1()