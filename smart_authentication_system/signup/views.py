from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
# Create your views here.


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        
        if password==confirm_password:
            user=User.objects.create(username=username,first_name=first_name,last_name=last_name,is_active=True)
            user.set_password(password)
            user.save()
            return render(request,'login/login.html')
    else:
        return render(request,'signup/signup.html')


    
def logout(request):
   
    logout(request)
    return render(request,'login/logout.html')