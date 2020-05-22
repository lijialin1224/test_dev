from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

#用来写请求的处理逻辑的

def hello(requests):
    return HttpResponse("ok")

#登录

def login(request):
#返回登录页面
    if request.method=="GET":
        return render(request,"login.html")

#登录动作处理
    print("请求方法:",request.method)
    if request.method=="POST":
        username=request.POST.get("username","")
        password=request.POST.get("password","")
        if username == "" or password=="":
            return render(request,"login.html",{
                "error":'用户名或密码为空'
            })
        user=auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect("/manage/")
        else:
            return render(request,"login.html",{
                "error":"用户名或密码错误"
            })
@login_required     
def mange(request):
        return render(request,"manage.html")