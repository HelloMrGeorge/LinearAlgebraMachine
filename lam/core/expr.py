from lam.core import output
'''
描述数学表达式元素的模块
'''
class Monomial(output.htmlOutPut):
    '''
    创建单项式这一数学元素对象的类。
    '''
    def __init__(self, element, sign: str ='+', ) -> None:
        '''
        sign:   表示单项式前面的符号
        element: 表示单项式的中心元素
        '''
        self.sign = sign
        self.element = element
        return

    def htmlStr(self) -> str:
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