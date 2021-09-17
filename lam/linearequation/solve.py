from sympy import *
from lam.linearequation import reduction

class EquationSolve(reduction.MatrixReduction):

    def __init__(self, matrix: MatrixBase) -> None:
        #matrix输入线性方程增广矩阵
        super().__init__(matrix)

        #x,equ存储方程的变量和符号化的矩阵
        self.x = zeros(self.matrix.shape[1]-1, 1) 
        self.equ_list = zeros(self.matrix.shape[0], 1)
        return

    def get_course(self) -> list:
        #获得求解过程
        self.echelon_form()
        self.symbolize_equ()
        self.solve_pivot()
        self.sub_var()
        return self.course
    
    def symbolize_equ(self) -> None:
        #将增广矩阵符号化，变为易读的公式形式
        for i in range(self.matrix.shape[1]-1):
            self.x[i] = symbols(f'x_{i+1}')
        for i in range(self.matrix.shape[0]):
            left = self.x.dot(self.matrix[i, :-1])
            self.equ_list[i] = Eq(left ,self.matrix[i,-1] ,evaluate=False)
        
        return  self.course.append(self.equ_list.copy())

    def solve_pivot(self) -> None:
        assert self.is_solvable
        #解非自由变量，使得方程左边只有一个元素
        for rowInd in range(self.matrix.shape[0]):
            if self.equ_list[rowInd].args[0] != 0:    #不计算只有0的行
                pivot = self.x[self.pivot_Ind(self.matrix[rowInd, :])]
                self.equ_list[rowInd] = Eq(pivot, solve(self.equ_list[rowInd], pivot)[0], evaluate=False)
        
        return  self.course.append(self.equ_list.copy())

    def sub_var(self) -> None:
        #变量代换，在解完非自由变量后，依次代换掉方程右边非自由变量的值
        n = 1   #计数器，用于给要替换的未知元个数记数
        for rowInd in range(self.matrix.shape[0]-2, -1, -1):          
            if self.equ_list[rowInd+1].args[0] != 0:
                n = n + 1
                right = self.equ_list[rowInd].args[1]
                for i in range(1,n):
                    right = right.subs(self.equ_list[rowInd+i].args[0], self.equ_list[rowInd+i].args[1])
                self.equ_list[rowInd] = Eq(self.equ_list[rowInd].args[0], right, evaluate=False)
        
        return  self.course.append(self.equ_list.copy())

    @property
    def is_solvable(self) -> bool:
        #定义了是否可求解的属性
        flag = True
        for rowInd in range(self.matrix.shape[0]-1, -1, -1):
            if self.pivot_Ind(self.matrix[rowInd, :]) == self.matrix.shape[1]-1:
                flag = False
                break
        return flag

    # def solution(self) -> list:
    #     try:
    #         if not self.matrix.is_echelon:
    #             raise ValueError
    #     except:
    #         print('矩阵不是阶梯型')

    #     #先解非自由变量，使得方程左边只有一个元素
    #     self.symbolize_equ()
    #     for rowInd in range(self.matrix.shape[0]):
    #         equ = self.equ[rowInd]
    #         if equ.args[0] != 0:
    #             row = self.matrix[rowInd, :]
    #             pivot = self.x[self.pivot_Ind(row)]
    #             self.equ[rowInd] = Eq(pivot, solve(equ, pivot)[0], evaluate=False)
    #     self.course.append(self.equ.deepcopy())

    #     #再依次用自由变量表示
    #     n = 1   #计数器，用于给要替换的未知元个数记数
    #     for rowInd in range(self.matrix.shape[0]-2, -1, -1):          
    #         if self.equ[rowInd+1].args[0] != 0:
    #             n = n + 1
    #             right = self.equ[rowInd].args[1]
    #             for i in range(1,n):
    #                 right = right.subs(self.equ[rowInd+i].args[0], self.equ[rowInd+i].args[1])
    #             # right = right.subs(self.equ[rowInd+1].args[0], self.equ[rowInd+1].args[1])
    #             self.equ[rowInd] = Eq(self.equ[rowInd].args[0], right)
    #     return

        

