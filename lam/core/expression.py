from lam.core import output
'''
描述数学表达式元素的模块
'''
class Monomial(output.htmlOutPut):
    '''
    创建单项式这一数学元素对象的类。
    '''
    def __init__(self, element, coefficient = 1, sign: str ='+', ) -> None:
        '''
        sign:   表示单项式前面的符号
        coefficient 表示单项式的系数，存储纯数值时系数为1，而数值存储在中心元素中
        element: 表示单项式的中心元素
        '''
        self.coefficient = coefficient
        self.sign = sign
        self.element = element
        return

    def htmlStr(self) -> str:
        if self.coefficient != 1:
            text = output.htmlStr(self.sign) + output.htmlStr(self.coefficient) + output.htmlStr(self.element)
        else:
            text = output.htmlStr(self.sign) + output.htmlStr(self.element)
        return text

class Polynomial(list, output.htmlOutPut):
    '''
    创建多项式的类，它继承列表类，创建的对象是单项式的列表
    '''
    def append(self, __object: Monomial) -> None:
        return super().append(__object)

    def htmlStr(self) -> str:
        text = ''
        for x in self:
            text = text + output.htmlStr(x)
        return text

class Equation(output.htmlOutPut):
    '''
    创建数学元素——等式对象的类
    '''
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def htmlStr(self) -> str:
        text = output.htmlStr(self.left) + '=' + output.htmlStr(self.right)
        return text

    def htmlStrAlign(self) -> str:
        '''
        带对齐符的网页文本输出
        '''
        text = output.htmlStr(self.left) + '&=' + output.htmlStr(self.right)
        return text

class EquGroup(list, output.htmlOutPut):
    '''
    创建数学元素——方程组对象的类， 它是等式对象的容器
    '''
    def append(self, __object: Equation) -> None:
        return super().append(__object)

    def htmlStr(self) -> str:
        text = ''
        for x in self:
            text = text + x.htmlStrAlign() + '\\\\'
        text = text[:-2]    #取消最后两个反斜杠，避免换行
        return text    