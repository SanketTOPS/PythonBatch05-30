from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    #return HttpResponse("Hello Students!")
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
