import json
from django.http import JsonResponse
from django.shortcuts import render
from lam.linspace import MLIG
from lam.readtext.readtext import readtext

# Create your views here.

def MLIGSolver(request):
    mat = readtext(json.loads(request.body)['matrix'])
    ls = []
    for i in range(mat.shape[0]):
        ls.append(mat[i, :])
    jsdata = MLIG.MLIGSolver(ls).dict()
    return JsonResponse(jsdata)

def MLIGSolverPage(request):
    return render(request, 'linspace/MLIGSolverPage.html')