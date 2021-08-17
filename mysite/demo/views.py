from django.shortcuts import render
from django.http import JsonResponse
from . import multi
#尚未打包安装，请先将工具包加入环境变量
import sys
sys.path.append('D:\\Share\\work')
from lam.core.interpreter import interpret
import lam.core.gausselim as gaussE
# Create your views here.

def demo(request):
    return render(request, 'demo/demoPage.html')

def answer(request):
    ans = multi.inv(request.GET.get('matrix'))
    ans = str(ans)
    return JsonResponse({'matrix': ans})

def gaussElim(request):
    return render(request, 'demo/GEMPage.html')

def guassAns(request):
    mat = interpret(request.GET.get('matrix'))
    process = gaussE.gaussElim(mat)
    lis = []
    for step in process.stepList:
        lis.append(str(step.matList[0]))
    return JsonResponse({'matLis': lis})