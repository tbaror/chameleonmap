from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.

class LoginUsers(LoginView):
    
    template_name =
