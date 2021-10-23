from django.shortcuts import render
from django.http import JsonResponse

#尚未打包安装，请先将工具包加入环境变量，已改为相对路径，已在init文件处引入
# import sys
# from pathlib import Path
# lampy_dir = Path(__file__).resolve().parent.parent.parent
# sys.path.append(str(lampy_dir))

# from lam.core import input, expression
# from lam.det import det
from lam.linearequation import outtext

from .formtest import formtest
# Create your views here.

def demo(request):
    return render(request, 'demo/demoPage.html')

def answer(request):
    return render(request, 'demo/answerPage.html')

def gaussElim(request):
    return render(request, 'demo/GEMPage.html')

def guassAns(request):
    lis = 0
    return JsonResponse({'matLis': lis})

def testView(request):
    #测试页面
    text = outtext.main()
    # text = formtest()
    return render(request, 'demo/testView.html', {'text': text})

def testAnswer(request):
    # mat = request.POST.get('matrix')
    # mat = input.Interpreter.intepretAs('Determinant', mat)
    # mono = expression.Monomial(mat)
    # ans = expression.Polynomial()
    # ans.append(mono)
    # ans = det.LEbyStep(ans)
    # return render(request, 'demo/testAnswer.html', {'answer': ans.htmlStr()})
    pass