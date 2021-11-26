from django.shortcuts import render
from output import slvdeter
from django.http.response import HttpResponse
from django.core import serializers
import json
import logging
logging.basicConfig(level=logging.DEBUG, filename='mylog.txt', filemode='w')
# Create your views here.
from django.http import JsonResponse
def determinant(request):
    return render(request, 'demo/deterPage.html')


def deteranswer(request):
    mat = json.loads(request.body)['matrix']
    jsondata = slvdeter.slvdeter(mat)
    # 将字符串类型数据转换为json
    logging.debug(jsondata)
    logging.debug(type(jsondata))
    return JsonResponse(jsondata, safe=False)

