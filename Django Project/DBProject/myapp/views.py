from django.shortcuts import redirect, render
from .forms import userForm,updateForm
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

def updatedata(request,id):
    stid=userData.objects.get(id=id)
    if request.method=='POST':
        updateuser=updateForm(request.POST)
        if updateuser.is_valid():
            updateuser=updateForm(request.POST,instance=stid)
            updateuser.save()
            print("Your data has been updated!")
            return redirect('confirm')
        else:
            print(updateuser.errors)
    return render(request,'updatedata.html',{'user':userData.objects.get(id=id)})

def deletedata(request,uid):
    stid=userData.objects.get(id=uid)
    userData.delete(stid)
    return redirect('confirm')