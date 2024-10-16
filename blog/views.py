from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages
from .forms import CreateUser, LoginUser
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

