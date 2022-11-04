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

            uid=userSignup.objects.get(username=unm)
            print("USerID:",uid.id)
            user=userSignup.objects.filter(username=unm,password=pas)
            if user: #true
                request.session['user']=unm #session created
                request.session['userid']=uid.id
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

def profile(request):
    uid=request.session.get('userid')
    user=request.session.get('user')
    cuser=userSignup.objects.get(id=uid)
    if request.method=='POST':
        updateuser=usersignupForm(request.POST)
        if updateuser.is_valid():
            updateuser=usersignupForm(request.POST,instance=cuser)
            updateuser.save()
            print("Your profile has been updated!")
        else:
            print(updateuser.errors)
    return render(request,'profile.html',{'user':user,'cuser':userSignup.objects.get(id=uid)})
