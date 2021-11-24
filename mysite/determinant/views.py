from django.shortcuts import render
from output import slvdeter
from django.http.response import HttpResponse
from django.core import serializers
from django.http import JsonResponse

import os

# Create your views here.

def determinant(request):
    return render(request, 'demo/demoPage.html')


def answer(request):
    mat = request.POST.get('matrix')
    slvdeter.slvdeter(mat)
    # 将字符串类型数据转换为json
    with open('./test_data.json', 'r') as json_file:
        jsondata = json_file.read()
    return JsonResponse(jsondata, safe=False)

def test(request):
    mat = request.POST.get('matrix')
    return JsonResponse({'matrix': mat}, safe=False)

