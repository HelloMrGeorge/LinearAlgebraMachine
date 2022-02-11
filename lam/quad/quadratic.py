import logging
from typing import List
import sympy as sp
from sympy.matrices.dense import MutableDenseMatrix
from lam.quad.quadbase import *

logging.basicConfig(level=logging.DEBUG)

class QuadSolver:

    def __init__(self, mat: MutableDenseMatrix, evaluate = True) -> None:
        self.mat: MutableDenseMatrix = mat
        self.trans: List[MutableDenseMatrix] = [] #存储变数替换的矩阵
        self.mark: List[str] = [] #存储变数替换矩阵的类型
        self.result: List[MutableDenseMatrix] = [] #存储每一步变数替换的结果

        # 不显示的元素
        self.is_symmetry: bool = True if self.mat.is_symmetric() else False # mat是否对称，sympy自带的判断函数除了是否外还存在未知这个选项，故不能直接使用
        self.evaluate = False
        if evaluate:
            self.get_course()
            self.evaluate = True

    def get_course(self) -> None:
        if not self.evaluate:
            if self.is_symmetry == False:
                raise Exception('不是对称矩阵')
            
            mat: MutableDenseMatrix = self.mat.copy()
            while mat.is_diagonal() == False:
                tran, mark = next_quad_op(mat)
                mat = tran.T @ mat @ tran
                self.trans.append(tran)
                self.result.append(mat)
                self.mark.append(mark)

    
    def dict(self):
        '''
        返回该对象latex文本化的字典对象
        '''
        if not self.evaluate:
            self.get_course()

        js = {}
        js['mat'] = sp.latex(self.mat)
        js['mark'] = self.mark

        js['trans'] = []
        for m in self.trans:
            js['trans'].append(sp.latex(m))

        js['result'] = []
        for m in self.result:
            js['result'].append(sp.latex(m))

        self.js = js
        return self.js

