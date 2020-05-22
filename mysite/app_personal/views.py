from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

#用来写请求的处理逻辑的

def hello(requests):
    return HttpResponse("ok")

#登录

def login(request):
    return render(request,"login.html")
def login_action(request):
#登录动作处理
    print("请求方法:",request.method)
    if request.method=="POST":
        username=request.POST.get("username","")
        password=request.POST.get("password","")
        if username == "" or password=="":
            return render(request,"login.html",{
                "error":'用户名或密码为空'
            })
        if username=="admin" and password=="admin123":
            return render(request,"manage.html",{
            })
        else:
            return render(request,"login.html",{
                "error":"用户名或密码错误"
            })