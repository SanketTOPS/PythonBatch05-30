from dataclasses import fields
from pyexpat import model
from django import forms
from .models import userData

class userForm(forms.ModelForm):
    class Meta:
        model=userData
        fields='__all__'


class updateForm(forms.ModelForm):
    class Meta:
        model=userData
        fields=['name','email','mobile']
