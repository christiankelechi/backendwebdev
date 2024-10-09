from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
# Create your views here.
from signup.forms import RegistrationForm
from django.shortcuts import render
from signup.forms import RegistrationForm,ExaminationForm

def signup(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # handle successful registration logic
    return render(request, 'signup/signup.html', {'form': form})


def logout(request):
    logout(request)
    return render(request,'login/logout.html')

def welcome_page(request):
    return HttpResponse("Welcome Favour")