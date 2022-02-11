from django.shortcuts import render
from django.http import JsonResponse
from output import slveigen
import json

import logging
logging.basicConfig(level=logging.DEBUG,filename='mylog.txt',filemode='w')

def eigen(request):
    return render(request, 'demo/eigenPage.html')

def eigenCourse(request):
    mat = json.loads(request.body)['matrix']
    jsondata=slveigen.slveigenCourse(mat)
    logging.debug(jsondata)
    return JsonResponse(jsondata, safe=False)

def eigenvectors(request):
    mat = json.loads(request.body)['matrix']
    jsondata=slveigen.slveigenvectors(mat)

    return JsonResponse(jsondata, safe=False)

def eigenvalue(request):
    mat = json.loads(request.body)['matrix']
    jsondata=slveigen.slveigenvalue(mat)

    return JsonResponse(jsondata, safe=False)

def eigencharpoly(request):
    mat = json.loads(request.body)['matrix']
    jsondata=slveigen.slveigengetcharpoly(mat)

    return JsonResponse(jsondata, safe=False)

def eigenvaluePage(request):
    return render(request,'eigenvalue.html')
