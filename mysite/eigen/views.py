from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from output import slvdeter
def eigen(request):
    return render(request, 'demo/eigenPage.html')
def eigenanswer(request):
    mat = request.POST.get('matrix')
    jsondata=slvdeter.slvdeter_eigen(mat)
    print(type(jsondata))
    return JsonResponse(jsondata, safe=False)

