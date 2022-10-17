from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def newuser(request):
    return render(request,'newuser.html')