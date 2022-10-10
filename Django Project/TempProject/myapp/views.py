from django.shortcuts import render
import random

# Create your views here.
def index(request):
    n={'num':random.randint(1111,9999)}
    #dt={'nm':'Nirav'} #context object
    #return render(request,'index.html',dt)
    #return render(request,'index.html',{'nm':'Ashok'})
    return render(request,'index.html',n)