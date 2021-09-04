from lam.core import ndmatrix, process

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
    矩阵环节类，它存储单个矩阵，
    常用于存储像高斯消元法，行列式变形等计算步骤，这些计算步骤往往只有每一步只有一个矩阵
    '''
    dtype = ndmatrix.NumMatrix  #定义储存的数据类型为数值矩阵

    def htmlOutPut(self) -> str:
        content = ''
        for i in self:
            assert isinstance(i, self.dtype)
            content = content + i.htmlOutPut()
        return content

class AlgStep(Step):
    '''
    代数环节类，它存储不含矩阵的代数式。
    '''
    dtype = {'operater': str, 'coefficient': float}

    def appendDic(self, operater, coefficient) -> None:
        #以字典形式添加数据，仅支持dtype类型的数据，dtype = {'operater': str, 'coefficient': float}
        return super().append({'operater':operater, 'coefficient':coefficient})


    def htmlOutPut(self) -> str: #定义存储的数据类型为(算符，系数)
        content = ''
        for i in self:
            content = content + i['operater'] + str(i['coefficient'])
        return content

class MatAlgStep(Step):
    '''
    矩阵代数环节类，它存储关于矩阵的代数式，
    常用于存储像Laplace展开计算行列式的值，矩阵四则运算等计算步骤，这些计算步骤往往可以列出一个个等式，每个等式都是关于矩阵的代数式。
    ''' 
    dtype = {'operater': str, 'coefficient': float, 'matrix': ndmatrix.NumMatrix}  #定义存储的数据类型为(算符，系数，数值矩阵)，仅作标记，暂无实际用途

    def htmlOutPut(self) -> str:
        content = ''
        for i in self:
            content = content + i['operater'] + str(i['coefficient']) + i['matrix'].htmlOutPut()
        return content

    def appendDic(self, operater, coefficient, matrix) -> None:
        #以字典形式添加数据，仅支持dtype类型的数据，dtype = {'operater': str, 'coefficient': float, 'matrix': ndmatrix.NumMatrix}
        return super().append({'operater':operater, 'coefficient':coefficient, 'matrix': matrix})

def htmlOutPut(__object) -> str:
    '''
    网页文本输出函数，兼容环节类和非环节类的输出
    '''
    if isinstance(__object, process.Step):
        return __object.htmlOutPut()
    else:
        text = f'${str(__object)}$'
        return text
