import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from lam.linspace import MLIG, lincombination
from mysite import matParser

# Create your views here.
def MLIGSolver(request):
    mat = matParser(json.loads(request.body)['matrix'])
    ls = []
    for i in range(mat.shape[0]):
        ls.append(mat[i, :])
    jsdata = MLIG.MLIGSolver(ls).dict()
    return JsonResponse(jsdata)

@ensure_csrf_cookie
def MLIGSolverPage(request):
    return render(request, 'linspace/MLIGSolverPage.html')


def LincombinationSolver(request):
    js = json.loads(request.body)
    mat = matParser(js['matrix'])
    vec = matParser(js['vector'])
    jsdata = lincombination.LincombinationSolver(mat, vec).dict()
    return JsonResponse(jsdata)

@ensure_csrf_cookie
def LincombinationSolverPage(request):
    return render(request, 'linspace/LincombinationSolverPage.html')