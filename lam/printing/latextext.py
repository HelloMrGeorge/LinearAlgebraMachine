import sympy as sp

class LatexText():
    #定义了一个输出latex文本的接口
    def latex(self) -> str:
        pass

def latex(obj):
    if isinstance(obj, LatexText):
        return obj.latex()
    else:
        return sp.latex(obj)