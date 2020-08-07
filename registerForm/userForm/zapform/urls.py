from django.conf import urls
from django.urls import path
from zapform import views

app_name = 'zapform'

urlpatterns = [
    path('login/', views.login, name ='login'),
    path('register/', views.register, name = 'register'),
    path('',views.index,name='index'),
]