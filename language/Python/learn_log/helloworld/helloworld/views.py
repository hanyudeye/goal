from django.http import HttpResponse

#    shortcuts 是 捷径 的意思
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world ! ")


def index(request):
    return HttpResponse("这是首页")


# 进入模板页面
def  runoob(request):
    context={}
    context['title']="菜鸟"

    context['list']=["鸡蛋","鸭蛋","鹅蛋","蠢蛋"]
    # return HttpResponse("这是首页")
    return render(request,'runoob.html',context)