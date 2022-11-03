from django.shortcuts import redirect, render
from .forms import usersignupForm,notesForm
from .models import userSignup
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            username=""
            newuser=usersignupForm(request.POST)
            if newuser.is_valid():
                username=newuser.cleaned_data.get('username')
                try:
                    unm=userSignup.objects.get(username=username)
                    print("Username is already exists.")   
                except userSignup.DoesNotExist:
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
                #print("Error....Plz try again!")
                messages.error(request,"Username or Password does not correct!")
    return render(request,'index.html')

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        mynote=notesForm(request.POST, request.FILES)
        if mynote.is_valid():
            mynote.save()
            print("Your notes has been uploaded!")
        else:
            print(mynote.errors)
    return render(request, 'notes.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')
