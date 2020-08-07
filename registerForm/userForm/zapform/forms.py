from django.db import models 
from django import forms 
from zapform.models import UserID, UserModel_form
from django.contrib.auth.models import User

class UserForm (forms.ModelForm):
    passward = models.CharField(max_length=20)
    class Meta():
        model = UserID
        fields = ('username','email')


class userInput_form(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model= User
        fields = ("username","password","email")

class UserUrl(forms.ModelForm):
    class Meta:
        model = UserModel_form
        fields = ('user_url',)        
