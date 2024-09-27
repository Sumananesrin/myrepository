from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

# Create your views here.

def members(request):
    return render(request,'index.html')
def hello(request):
    return render(request,'index2.html')

def geeks_view(request):
    context={
        "firstname":"sumana",
        "lastname":"nesrin",
    }
    return render(request,"context.html",context)
def forr_loop(request):
    context={
        "data": [1,2,3,4,5,6,7],}
    return render(request,"forloop.html",context)

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        # fullname = request.POST['fullname']
        # phone = request.POST['phone']


        if User.objects.filter(username=username).exists():
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            return redirect('register')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()

            return redirect('/')
    else:
        return render(request,'register.html')


def logi(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('logi')

    return render(request,'login.html')


def collections(request):
    return render(request,'collections.html')


def logout(request):
    auth.logout(request)
    return redirect('/')