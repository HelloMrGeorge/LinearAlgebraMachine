import json, sympy
from django.http import JsonResponse
from django.shortcuts import render
from sympy.abc import a
from lam.readtext.readtext import readtext
from lam.linequ import linequsolver, guasselimination, lambdalinequ, inverse

# Create your views here.

def GESolver(request):
    mat = json.loads(request.body)['matrix']
    mat = readtext(mat)
    jsdata = guasselimination.GESolver(mat).dict()
    return JsonResponse(jsdata)

def GESolverPage(request):
    return render(request, 'linequ/GESolverPage.html')


def LinequSolver(request):
    mat = json.loads(request.body)['matrix']
    mat = readtext(mat)
    jsdata = linequsolver.LinequSolver(mat[:, :-1], mat[:, -1]).dict()
    return JsonResponse(jsdata)

def LinequSolverPage(request):
    return render(request, 'linequ/LinequSolverPage.html')


def InverseSolver(request):
    mat = json.loads(request.body)['matrix']
    mat = readtext(mat)
    jsdata = inverse.InverseSolver(mat).dict()
    return JsonResponse(jsdata)

def InverseSolverPage(request):
    return render(request, 'linequ/InverseSolverPage.html')


def LambdaLinSolver(request):
    # mat = json.loads(request.body)['matrix']
    # mat = readtext(mat)
    mat = [
        [a, 1, 1, 1],
        [1, a, 1, a],
        [1, 1, a, a**2],
    ]
    mat = sympy.Matrix(mat)
    jsdata = lambdalinequ.LambdaLinSolver(mat, a).dict()
    return JsonResponse(jsdata)

def LambdaLinSolverPage(request):
    return render(request, 'linequ/LambdaLinSolverPage.html')