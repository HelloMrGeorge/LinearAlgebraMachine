from django.shortcuts import render
from django.http import JsonResponse
from lam.quad import quadratic
from mysite import matParser
import json


def QuadSolverPage(request):
    return render(request, 'quad/QuadSolverPage.html')

def QuadSolver(request):
    mat = matParser(json.loads(request.body)['matrix'])
    jsdata = quadratic.QuadSolver(mat).dict()
    return JsonResponse(jsdata)


def HurwitzSolverPage(request):
    return render(request, 'quad/HurwitzSolverPage.html')

def HurwitzSolver(request):
    mat = matParser(json.loads(request.body)['matrix'])
    jsdata = quadratic.HurwitzSolver(mat).dict()
    return JsonResponse(jsdata)