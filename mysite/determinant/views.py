from django.shortcuts import render
from output import slvdeter
from django.http.response import HttpResponse
from django.core import serializers
import json
# Create your views here.
from django.http import JsonResponse
def determinant(request):
    return render(request, 'demo/demoPage.html')


def answer(request):
    print(request)
    mat = request.POST.get('matrix')
    print(mat)
    slvdeter.slvdeter(mat)
    # 将字符串类型数据转换为json
    with open('../output/test_data.json', 'r') as json_file:
        jsondata = json_file.read()
    return JsonResponse(jsondata, safe=False)

def HOME(request):
    return render(request,'deter.html')
