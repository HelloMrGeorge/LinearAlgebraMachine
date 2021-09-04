from lam.core import process, output

class Monomial(process.Step):
    '''
    单项式类，用于生成单项式对象，定义单项式的各个要素
    '''
    def __init__(self, element, coefficient=1, operater='+', degree=1) -> None:
        self.element = element #中心元素，比如矩阵或者字母
        self.coefficient = coefficient  #系数，代数式中矩阵前的系数
        self.operater = operater    #运算符，单项式前面的运算符，加‘+’或者减‘-’
        self.degree = degree    #次数，中心元素的指数
        return

    def htmlOutPut(self) -> str:
        text =  output.htmlOutPut(self.operater) + output.htmlOutPut(self.coefficient)
        text = text + output.htmlOutPut(self.element) + output.htmlOutPut(self.degree)
        return text

class Polynomial(process.Step, list):
    '''
    多项式类，用于生成多项式对象，存储若干个单项式。
    仅建议用append方法添加元素。
    '''
    def append(self, __object) -> None:
        assert isinstance(__object, Monomial)
        return super().append(__object)


    