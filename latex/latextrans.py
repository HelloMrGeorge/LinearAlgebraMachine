import sympy as sp
from sympy.abc import *
from sympy.parsing.sympy_parser import parse_expr,standard_transformations,implicit_application,function_exponentiation

escape_dict = \
    {
        '\a': r'\a', '\b': r'\b', '\c': r'\c', '\f': r'\f', '\n': r'\n', '\r': r'\r', '\t': r'\t', '\v': r'\v',
               '\'': r'\'', '\"': r'\"', '\0': r'\0', '\1': r'\1', '\2': r'\2', '\3': r'\3', '\4': r'\4', '\5': r'\5',
               '\6': r'\6', '\7': r'\7', '\8': r'\8', '\9': r'\9','\\':r'\\'

     }


def raw(text):
    """Returns a raw string representation of text"""
    new_string = ''
    for char in text:
        try: new_string += escape_dict[char]
        except KeyError: new_string += char
    return new_string
def latextrans(formula:str):
    formula=raw(formula)

    formula=formula.split('{matrix}')[1]
    formula=formula.split('\end')[0]
    formula=formula.split(r'\\\\')[0:-1]
    matrix=[]
    for i in range(len(formula)):
        matrix.append([])
        matrix[i].append(formula[i].split('&'))
    result=matrix
    return result
def standard_transformation(matrix):
    if type(matrix)==list:
        for i in matrix:
            return 0
    else:
        return 0
print(latextrans('\left[ \begin{matrix}56&56&56&6\\5&4&2&1\\a&\alpha&\delta&\theta\\\gamma&\sqrt{\lambda}&\frac{\alpha}{\beta}&\sqrt{\frac{\chi}{\eta}}\\\end{matrix} \right] '))
