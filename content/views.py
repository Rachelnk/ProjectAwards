from turtle import title
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from awards import settings
from .forms import UpdateUserForm, UpdateProfileForm, AddPortfolioForm
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
def logout(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out!')
    return redirect(reverse('login'))

@login_required(login_url='login')
def index(request):
  portfolios = Portfolio.objects.all()
  return render(request, "index.html", {'portfolios':portfolios})

def register(request):
  if request.method == 'POST':
        context = {'has_error': False}
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords Do Not Match! Try Again')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username Already Exists! Choose Another One')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email Address Already Exists! Choose Another One')
            return redirect('register')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password1)
        user.save()        
  
  return render(request, 'register.html')

@login_required(login_url='login')
def addportfolio(request):
    form = AddPortfolioForm()
    if request.method == "POST":
        form = AddPortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.author = request.user
            portfolio.profile = request.user.profile
            portfolio.save()
            messages.success(request, 'Your Project Was Created Successfully!')
            return redirect('index')
        else:
            messages.error(request, "Your Project Wasn't Created!")
            return redirect('addportfolio')
    else:
        form = AddPortfolioForm()
    return render(request, 'addportfolio.html', {'form':form})

def portfoliodetails(request):
    project = Portfolio.objects.get(title=title)
    ratings = Rating.objects.filter(project = project.id).all()
    ratings_no = Rating.objects.filter(project = project.id)
    return render (request, 'portfolio_details.html', {'project': project , 'ratings': ratings, 'ratings_no':ratings_no})


@login_required(login_url='login')
def myprofile(request):
    return render(request, 'myprofile.html')
    
def userprofile(request):
    return render(request, 'userprofile.html')

@login_required(login_url='login')
def editprofile(request):
    return render(request, 'editprofile.html')

def search(request):
    return render(request, 'search_results.html')

@login_required(login_url='login')
def settings(request):
    return render(request, 'settings.html')


