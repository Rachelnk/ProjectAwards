from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from awards import settings
# from .forms import UpdateUserForm, UpdateProfileForm, AddPostForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Portfolio, Profile, Rating
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def loginUser(request):
  return render (request,'login.html')

@login_required(login_url='login')
def index(request):
  return render(request, "index.html")

def register(request):
  return render(request, 'register.html')


