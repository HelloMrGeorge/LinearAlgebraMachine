from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from output import slveigen
import logging
import json
logging.basicConfig(level=logging.DEBUG,filename='mylog.txt',filemode='w')
def eigen(request):
    return render(request, 'demo/eigenPage.html')
def eigenCourse(request):
    mat = json.loads(request.body)['matrix']
    jsondata=slveigen.slveigenvectorsCourse(mat)
    logging.debug(jsondata)
    logging.debug(type(jsondata))
    return JsonResponse(jsondata, safe=False)
def eigenvectors(request):
    mat = json.loads(request.body)['matrix']
    jsondata=slveigen.slveigenvectors(mat)
    logging.debug(jsondata)
    logging.debug(type(jsondata))
    return JsonResponse(jsondata, safe=False)
def eigenvalue(request):
    mat = json.loads(request.body)['matrix']
    jsondata=slveigen.slveigenvalue(mat)
    logging.debug(jsondata)
    logging.debug(type(jsondata))
    return JsonResponse(jsondata, safe=False)
def eigencharpoly(request):
    mat = json.loads(request.body)['matrix']
    jsondata=slveigen.slveigengetcharpoly(mat)
    logging.debug(jsondata)
    logging.debug(type(jsondata))
    return JsonResponse(jsondata, safe=False)