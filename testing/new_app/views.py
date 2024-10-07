from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "food.html" )

def members(request):
  template = loader.get_template('hello.html')
  return HttpResponse(template.render())