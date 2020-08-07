from django.shortcuts import render
from zapform.models import UserID,UserModel_form
from zapform import forms
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    # user_data= forms.UserForm()

    if request.method == "POST":
        user_data = forms.UserForm(request.POST)
        if user_data.is_valid():
            # I dont want to commit to the model or the database for now .
            user_data.save(commit=False)
            return register(request)
    return render(request, 'zapform/Login.html', context= {'user_form': user_data})

def register(request):

    return render(request, 'zapform/register.html')    


def index(request):
    register_bool = False

    if request.method == "POST":
        register_form = forms.userInput_form(request.POST)
        urlform = forms.UserUrl(request.POST)

        if register_form.is_valid() and urlform.is_valid():
            user = register_form.save()
            user.set_password(user.password)
            user.save()

            urlset = urlform.save(commit=False)
            urlset.user = user

            urlset.save()


            register_bool = True
        else:
            print(register_form.errors)
    else:
        register_form = forms.userInput_form()
        urlform = forms.UserUrl()           
    return render(request, 'zapform/index.html', context={"register_form":register_form,"register_form":register_form,"urlform":urlform})