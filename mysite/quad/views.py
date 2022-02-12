from django.shortcuts import render
from django.http import JsonResponse
from output import slvquad
import json

import logging
logging.basicConfig(level=logging.DEBUG,filename='mylog.txt',filemode='w')
def quad(request):
    return render(request, 'demo/quadPage.html')
def quadCourse(request):
    mat = json.loads(request.body)['matrix']
    jsondata=slvquad.slvget_course(mat)
    logging.debug(jsondata)
    return JsonResponse(jsondata, safe=False)

