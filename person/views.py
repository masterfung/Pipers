from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

# Create your views here.


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'registration/login.html')


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')


@login_required
def profile(request):
    return render(request, 'profile/profile.html')