class Step():
    '''
    环节接口，将某些数学对象描述为一个环节，用于将这些数学元素文本化。
    '''
    def htmlOutPut(self) -> str:
        pass

class Process(list, Step):
    '''
    过程对象，它由多个环节组合而成，本身也可视为一个大环节
    仅建议用append方法添加元素。
    '''
    def append(self, __object) -> None:
        assert isinstance(__object, Step)
        return super().append(__object)

    def htmlOutPut(self) -> str:
        text = ''
        for x in self:
            assert isinstance(x, Step)
            text = text + x.htmlOutPut()
        return text
