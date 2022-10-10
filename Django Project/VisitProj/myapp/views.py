from glob import glob
from django.shortcuts import render

# Create your views here.
n=1
def index(request):
    global n
    n+=1
    return render(request,'index.html',{'num':n})