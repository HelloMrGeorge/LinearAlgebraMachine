from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from output import slvdeter
import logging
logging.basicConfig(level=logging.DEBUG,filename='mylog.txt',filemode='w')
def eigen(request):
    return render(request, 'demo/eigenPage.html')
def eigenanswer(request):
    mat = request.POST.get('matrix')
    jsondata=slvdeter.slvdeter_eigen(mat)
    logging.debug(jsondata)
    logging.debug(type(jsondata))
    return JsonResponse(jsondata, safe=False)

