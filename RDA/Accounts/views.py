from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate, get_user_model
from .forms import *

# Create your views here.


def login_page(request):
    return render(request, 'rda_frontend/login.html')


def register_page(request):
    # form = CreateUserForm()
    form = RegisterForm()
    if request.method == 'POST':
        # form = CreateUserForm(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../login')

    context = {'form': form}
    return render(request, 'rda_frontend/register.html', context)

