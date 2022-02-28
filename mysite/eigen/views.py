from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from lam.eigen import eigen
from mysite import matParser
from django.http import JsonResponse
import json

def EigenValueSolver(request):
    mat = json.loads(request.body)['matrix']
    mat = matParser(mat)
    jsdata = eigen.EigenValueSolver(mat).dict()
    return JsonResponse(jsdata)

@ensure_csrf_cookie
def EigenValueSolverPage(request):
    return render(request, 'eigen/EigenValueSolverPage.html')


def EigenVectorSolver(request):
    mat = json.loads(request.body)['matrix']
    mat = matParser(mat)
    jsdata = eigen.EigenVectorSolver(mat).dict()
    return JsonResponse(jsdata)

@ensure_csrf_cookie
def EigenVectorSolverPage(request):
    return render(request, 'eigen/EigenVectorSolverPage.html')