from django.shortcuts import redirect, render
from .forms import userForm
from .models import userData

# Create your views here.

def index(request):
    if request.method=='POST': #true
        user=userForm(request.POST)
        if user.is_valid():
            user.save()
            print("Your data has been saved!")
            return redirect('confirm')
        else: #false
            print(user.errors)
    return render(request,'index.html')

def confirm(request):
    data=userData.objects.all()
    return render(request,'confirm.html',{'data':data})

def updatedata(request):
    return render(request,'updatedata.html')

def deletedata(request,id):
    stid=userData.objects.get(id=id)
    userData.delete(stid)
    return redirect('confirm')