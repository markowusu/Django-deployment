from django.db import models
from django import forms
from django.contrib.auth.models  import User

# Create your models here.

class UserID(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=10)

    
#  This model is created for the user. 
class UserModel_form(models.Model):
    """ T"his  contains the username, password and the email for the user."""
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    user_url = models.URLField(blank=True,)

    def __str__(self):
        return self.user.username
