import json
from django.http import JsonResponse
from django.shortcuts import render
from lam.readtext.readtext import readtext
from lam.linequ import linequsolver, guasselimination, lambdalinequ

# Create your views here.

def GESolver(request):
    mat = json.loads(request.body)['matrix']
    mat = readtext(mat)
    jsdata = guasselimination.GESolver(mat).dict()
    return JsonResponse(jsdata)

def LinequSolver(request):
    mat = json.loads(request.body)['matrix']
    mat = readtext(mat)
    jsdata = linequsolver.LinequSolver(mat[:, :-1], mat[:, -1]).dict()
    return JsonResponse(jsdata)

def GESolverPage(request):
    return render(request, 'linequ/GESolverPage.html')