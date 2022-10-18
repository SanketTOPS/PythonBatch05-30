from django.shortcuts import redirect, render
from .forms import usersignupForm
from .models import userSignup
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST':

        unm=request.POST['username']
        pas=request.POST['password']
        user=userSignup.objects.filter(username=unm,password=pas)

        if user: #true
            print("Login Successfully!")
            request.session['user']=unm #create a session
            return redirect('home')
        else:
            print("Error!...Login fail.")
    return render(request,'index.html')

def newuser(request):
    if request.method=="POST":
        newuser=usersignupForm(request.POST)
        if newuser.is_valid(): #true
            newuser.save()
            print("Signup Successfully!")
            return redirect('home')
        else:
            print(newuser.errors)
    return render(request,'newuser.html')

def home(request):
    user=request.session.get('user') #session fetch
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')
