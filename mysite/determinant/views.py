from django.shortcuts import render
from output import slvdeter
from django.http import JsonResponse
from lam.readtext.readtext import readtext
from lam.determinant import determinant
import json

import logging
logging.basicConfig(level=logging.WARN, filename='mylog.txt', filemode='w')
# Create your views here.

def answer(request):
    mat = json.loads(request.body)['matrix']
    slvdeter.slvdeter(mat)
    # 将字符串类型数据转换为json
    with open('./test_data.json', 'r') as json_file:
        jsondata = json.load(json_file)
        logging.debug(jsondata)
        logging.debug(type(jsondata))
    return JsonResponse(jsondata)

def HOME(request):
    return render(request,'deter.html')

def DeterminantSolver(request):
    mat = readtext(json.loads(request.body)['matrix'])
    jsdata = determinant.DeterminantSolver(mat).dict()
    return JsonResponse(jsdata)

def DeterminantSolverPage(request):
    return render(request, 'determinant/DeterminantSolverPage.html')