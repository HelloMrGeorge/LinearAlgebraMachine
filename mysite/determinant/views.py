from django.shortcuts import render
from output import slvdeter
from django.http import JsonResponse
from lam.readtext.readtext import readtext
from lam.determinant import determinant
import json

import logging
logging.basicConfig(level=logging.WARN, filename='mylog.txt', filemode='w')
# Create your views here.

def DeterminantSolver(request):
    mat = readtext(json.loads(request.body)['matrix'])
    jsdata = determinant.DeterminantSolver(mat).dict()
    return JsonResponse(jsdata)

def DeterminantSolverPage(request):
    return render(request, 'determinant/DeterminantSolverPage.html')


def GaussDeterminantSolver(request):
    mat = readtext(json.loads(request.body)['matrix'])
    jsdata = determinant.GausseDeterminantSolver(mat).dict()
    return JsonResponse(jsdata)

def GaussDeterminantSolverPage(request):
    return render(request, 'determinant/GaussDeterminantSolverPage.html')