from django.shortcuts import render
from output import slvdeter
from django.http.response import HttpResponse
from django.core import serializers
import json
# Create your views here.
from django.http import JsonResponse
def determinant(request):
    return render(request, 'demo/deterPage.html')


def deteranswer(request):
    mat = request.POST.get('matrix')
    jsondata = slvdeter.slvdeter(mat)
    # 将字符串类型数据转换为json
    return JsonResponse(jsondata, safe=False)

