from dataclasses import fields
from pyexpat import model
from django import forms
from .models import userSignup,mynotes

class usersignupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'
        #fields=['username','password'] #cleaned_data

class notesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'