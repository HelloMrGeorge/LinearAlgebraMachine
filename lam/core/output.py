from lam.core import ndmatrix

class Step(list):
    '''
    环节类，它继承list类，抽象地定义了一个储存单步的输出内容的容器
    '''
    def htmlOutPut(self) -> str:
        return self.__str__()

class Process(list):
    '''
    过程类，它是环节类的容器
    '''
    def htmlOutPut(self) -> str:
        content = ''
        for i in self:
            assert isinstance(i, Step)
            content = content + i.htmlOutPut()
        return content

class MatrixStep(Step):
    '''
    矩阵环节类，它存储矩阵，
    常用于存储像高斯消元法，行列式变形等计算步骤，这些计算步骤往往只有每一步只有一个矩阵
    '''
    dtype = ndmatrix.NumMatrix  #定义储存的数据类型为数值矩阵

    def htmlOutPut(self) -> str:
        content = ''
        for i in self:
            assert isinstance(i, self.dtype)
            content = content + i.htmlOutPut()
        return content

class MatAlgStep(Step):
    '''
    矩阵代数环节类，它存储关于矩阵的代数式，
    常用于存储像Laplace展开计算行列式的值，矩阵四则运算等计算步骤，这些计算步骤往往可以列出一个个等式，每个等式都是关于矩阵的代数式。
    ''' 
    dtype = {'operater': str, 'coefficient': float, 'matrix': ndmatrix.NumMatrix}  #定义存储的数据类型为(算符，系数，数值矩阵)

    def htmlOutPut(self) -> str:
        content = ''
        for i in self:
            assert isinstance(i['operater'], self.dtype['operater']) and isinstance(i['coefficient'], self.dtype['coefficient']) and isinstance(i['matrix'], self.dtype['matrix'])
            content = content + i['operater'] + str(i['coefficient']) + i['matrix'].htmlOutPut()
        return content