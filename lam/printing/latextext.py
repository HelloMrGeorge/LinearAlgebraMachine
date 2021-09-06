import sympy as sp
from sympy.printing.latex import LatexPrinter

class LatexText:
    #定义了一个输出latex文本的接口
    def latex(self) -> str:
        pass

def latex(expr, **settings):
    str = LatexPrinter(settings)
    str._delim_dict['|'] = '|'
    return str.doprint(expr)
