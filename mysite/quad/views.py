from django.shortcuts import render
from django.http import JsonResponse
from lam.quad import quadratic
from latex.parser import matParser
from lam.readtext.readtext import readtext
import json

import logging
logging.basicConfig(level=logging.DEBUG,filename='mylog.txt',filemode='w')

# def quad(request):
#     return render(request, 'demo/quadPage.html')
    
# def quadCourse(request):
#     mat = json.loads(request.body)['matrix']
#     jsondata=slvquad.slvget_course(mat)
#     logging.debug(jsondata)
#     return JsonResponse(jsondata, safe=False)

# 新加入项
def QuadSolverPage(request):
    return render(request, 'quad/QuadSolverPage.html')

def QuadSolver(request):
    # mat = matParser(json.loads(request.body)['matrix'])
    mat = readtext(json.loads(request.body)['matrix'])
    jsdata = quadratic.QuadSolver(mat).dict()
    return JsonResponse(jsdata)

