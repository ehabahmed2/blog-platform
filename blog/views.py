from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages
from .forms import CreateUser, LoginUser, UpdateProfile
from .models import UserProfile
from django.contrib.auth import get_user_model


from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



# users profile
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def register_user(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = CreateUser()
    return render(request, 'users/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginUser(request.POST)
        if form.is_valid():
            # authenticate the user 
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                # login user 
                login(request, user)
                messages.success(request, "You're logged in!")
                return redirect('home')
            else:
                messages.info(request, 'Invalid email or password')
    else:
        form = LoginUser()
    return render(request, 'users/login.html', {'form': form})

def update_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':  
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password ')
                return redirect('home')
        else:
            form = PasswordChangeForm(request.user)
    else:
        messages.error(request, 'You must be logged in')
        return redirect('home')
    return render(request, 'users/update_pass.html', {'form':form})

User = get_user_model()
# Update user profile
def user_profile(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UpdateProfile(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, "Your details are saved successfully!")
            return redirect('user_profile')
    else:
        messages.info(request, 'You must be logged in')
        return redirect('home')
    return render(request, 'users/user_profile.html', {'form': form})



