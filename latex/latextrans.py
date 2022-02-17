import sympy as sp
from sympy.abc import *
from sympy.parsing.latex import parse_latex
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
    formula=formula.split('{matrix}')[1]
    formula=formula.split('\end')[0]
    print(formula)
    formula=formula.split(r'\\')[0:-1]
    matrix=[]
    for i in range(len(formula)):
        matrix.append(formula[i].split('&'))
    result=matrix
    return result
def standard_transformation(matrix:list):
    print(matrix)
    result=[]
    for i in range(len(matrix)):
        result.append([])
        for j in range(len(matrix[0])):
            print(matrix[i][j])
            result[i].append(parse_latex(matrix[i][j]))
    return result
