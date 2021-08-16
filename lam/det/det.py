from lam.core import gausselim, core
import numpy

def triDet(mat):
    #计算三阶行列式
    val = numpy.linalg.det(mat)
    return val