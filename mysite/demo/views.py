from django.shortcuts import render
from django.http import JsonResponse
#尚未打包安装，请先将工具包加入环境变量
import sys
sys.path.append('D:\\Share\\work')
from lam.core import interpreter, gausselim
# Create your views here.

def demo(request):
    return render(request, 'demo/demo3.html')

def answer(request):
    mat = request.POST.get('matrix')
    ans = interpreter.interpret(mat)
    ans = gausselim.gaussElim(ans)
    ans = str(ans)
    return render(request, 'demo/answer3.html', {'answer': ans})

def gaussElim(request):
    return render(request, 'demo/GEMPage.html')

def guassAns(request):
    mat = interpreter.interpret(request.GET.get('matrix'))
    process = gausselim.gaussElim(mat)
    lis = []
    for step in process.stepList:
        lis.append(str(step.matList[0]))
    return JsonResponse({'matLis': lis})