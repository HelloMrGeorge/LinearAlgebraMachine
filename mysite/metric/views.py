import json
from django.http import JsonResponse
from django.shortcuts import render
from lam.readtext.readtext import readtext
from lam.metric import schmidt

# Create your views here.

def SchmidtVectorSolver(request):
    mat = readtext(json.loads(request.body)['matrix'])
    jsdata = schmidt.SchmidtVectorSolver(mat).dict()
    return JsonResponse(jsdata)

def SchmidtVectorSolverPage(request):
    return render(request, 'metric/SchmidtVectorSolverPage.html')