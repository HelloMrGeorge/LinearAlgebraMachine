from django.shortcuts import render
from django.http import JsonResponse
from mysite import matParser, exprParser
from lam.poly import poly
import json

# Create your views here.

def PolySolverPage(request):
    return render(request, 'poly/PolySolverPage.html')

def PolySolver(request):
    js = json.loads(request.body)
    mat = matParser(js['matrix'])
    var = exprParser(js['var'])
    expr = exprParser(js['poly'])
    jsdata = poly.PolySolver(mat, var, expr).dict()
    return JsonResponse(jsdata)