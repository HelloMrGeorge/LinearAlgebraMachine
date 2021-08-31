from django.shortcuts import render
from django.http import JsonResponse
#尚未打包安装，请先将工具包加入环境变量
import sys
# sys.path.append('D:\\Share\\work')
sys.path.append('F:\myWeb\ProjectLam')
from lam.core import input, GE, expression
from lam.det import det
# Create your views here.

def demo(request):
    return render(request, 'demo/demoPage.html')

def answer(request):
    mat = request.POST.get('matrix')
    ans = input.interpret(mat)
    ans = GE.gaussElim(ans)
    ans = str(ans)
    return render(request, 'demo/answerPage.html', {'answer': ans})

def gaussElim(request):
    return render(request, 'demo/GEMPage.html')

def guassAns(request):
    mat = input.interpret(request.GET.get('matrix'))
    process = GE.gaussElim(mat)
    lis = []
    for step in process.stepList:
        lis.append(str(step.matList[0]))
    return JsonResponse({'matLis': lis})

def testView(request):
    return render(request, 'demo/testView.html')

def testAnswer(request):
    mat = request.POST.get('matrix')
    mat = input.Interpreter.intepretAs('Determinant', mat)
    mono = expression.Monomial(mat)
    ans = expression.Polynomial()
    ans.append(mono)
    ans = det.LEbyStep(ans)
    return render(request, 'demo/testAnswer.html', {'answer': ans.htmlStr()})