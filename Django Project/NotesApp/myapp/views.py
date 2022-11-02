from django.shortcuts import redirect, render
from .forms import usersignupForm
from .models import userSignup
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=usersignupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("User created successfully!")
                return redirect('notes')
            else:
                print(newuser.errors)
                #return messages("Error! Somthing went wrong.")
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            user=userSignup.objects.filter(username=unm,password=pas)
            if user: #true
                request.session['user']=unm #session created
                print("Login Successfully!")
                return redirect('notes')
            else:
                print("Error....Plz try again!")
    return render(request,'index.html')

def notes(request):
    user=request.session.get('user')
    return render(request, 'notes.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')
