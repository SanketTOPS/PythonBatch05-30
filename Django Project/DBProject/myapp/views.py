from django.shortcuts import redirect, render
from .forms import userForm

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
    return render(request,'confirm.html')