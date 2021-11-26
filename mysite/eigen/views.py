from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from output import slveigen
import logging
import json
logging.basicConfig(level=logging.DEBUG,filename='mylog.txt',filemode='w')
def eigen(request):
    return render(request, 'demo/eigenPage.html')
def eigenanswer(request):
    mat = json.loads(request.body)['matrix']
    jsondata=slveigen.slvdeter_eigen(mat)
    logging.debug(jsondata)
    logging.debug(type(jsondata))
    return JsonResponse(jsondata, safe=False)

