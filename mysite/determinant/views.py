from django.shortcuts import render
from output import slvdeter
from django.http import JsonResponse
import json

import logging
logging.basicConfig(level=logging.WARN, filename='mylog.txt', filemode='w')
# Create your views here.

def determinant(request):
    return render(request, 'demo/deterPage.html')

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
