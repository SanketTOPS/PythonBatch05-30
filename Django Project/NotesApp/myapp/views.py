from django.shortcuts import redirect, render
from .forms import usersignupForm,notesForm,feedbackForm
from .models import userSignup
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from NotesApp import settings
import requests
import random

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

                    # Email Send Code
                    sub="Welcome!"
                    msg=f"Hello User,\n\nWelcome to NotesApp.\nYour account has been created with us!\nEnjoy our services.\n\nThanks & Regards\n+91 9724799469 | query@notesapp.com"
                    #from_ID="djangotestmail2021@gmail.com"
                    from_ID=settings.EMAIL_HOST_USER
                    #to_ID=['dishu.vora@gmail.com','sanketchauhanios@gmail.com']
                    to_ID=[request.POST['username']]
                    send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
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

                otp=random.randint(1111,9999)
                # SMS Sending
                """url = "https://www.fast2sms.com/dev/bulkV2"
                querystring = {"authorization":"PSqGhvu5BkQv1WEvvWH6PIgV0vr1IcOIEzgsN1fZMHFG0WJapJ1hGGIwYfq8","variables_values":f"{otp}","route":"otp","numbers":"9879316741,9724799469"}
                headers = {
                    'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)"""

                url = "https://www.fast2sms.com/dev/bulkV2"

                querystring = {"authorization":"PSqGhvu5BkQv1WEvvWH6PIgV0vr1IcOIEzgsN1fZMHFG0WJapJ1hGGIwYfq8","message":f"Dear User\nYour account has been logged in with newer version of platform.\nIf you so ignore this sms.\nThank & Regards\nNotesApp Team","language":"english","route":"q","numbers":"9879316741,9724799469"}
                headers = {
                    'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)

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

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        sendfeedback=feedbackForm(request.POST)
        if sendfeedback.is_valid():
            sendfeedback.save()
            print("Your feedback has been submitted!")
        else:
            print(sendfeedback.errors)
    return render(request,'contact.html')
