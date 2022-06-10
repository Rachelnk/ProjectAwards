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
  if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)     

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username Does Not Exist! Choose Another One')
            return redirect('login')

        if user is None:
            messages.error(request, 'Username/Password Is Incorrect!! Please Try Again')
            return redirect('login')

        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
  return render (request,'login.html')

@login_required(login_url='login')
def index(request):
  return render(request, "index.html")

def register(request):
  return render(request, 'register.html')


