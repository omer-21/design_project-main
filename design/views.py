from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'design/index.html')
def dn(request):
    if request.method=='POST':
        #setAttribute2database
        print(request.POST)
        print("setdn")
        return HttpResponse('{"POST":"POST"}')   
    else:
        print("getdn")
        return render(request,'design/design.html')



def WW(request):
    if request.method=='POST':
        #setAttribute2database
        print(request.POST)
        print("setww")
        return HttpResponse('{"POST":"POST"}')   
    else:
        print("getWW")
        return render(request,'design/warp-weft-def.html')

def sw(request):
    if request.method=='POST':
        #setAttribute2database
        print(request.POST)
        print("setsw")
        return HttpResponse('{"POST":"POST"}')   
    else:
        print("getWW")
        return render(request,'design/sw.html')


def cw(request):
    if request.method=='POST':
        #setAttribute2database
        print(request.POST)
        print("setcw")
        return HttpResponse('{"POST":"POST"}')   
    else:
        print("getcw")
        return render(request,'design/cw.html')


def ld(request):
    if request.method=='POST':
        #setAttribute2database
        print(request.POST)
        print("setwld")
        return HttpResponse('{"POST":"POST"}')   
    else:
        print("getld")
        return render(request,'design/ld.html')


def ex(request):
    if request.method=='POST':
        #setAttribute2database
        print(request.POST)
        print("setex")
        return HttpResponse('{"POST":"POST"}')   
    else:
        print("getex")
        return render(request,'design/ex.html')






def setww(request):
    print(request.method)
    if request.method=='POST':
        #setAttribute2database
        print(request.POST)
        print("setww")
    return HttpResponse('{"POST":"POST"}')

def getValue(request):
    print(request.method)
    if request.method=='GET':
        print(request)
        return  HttpResponse ('{"get":"get"}')
    if request.method=='POST':
        return  HttpResponse('{"POST":"POST"}')    
    return HttpResponse('scdsafce')
