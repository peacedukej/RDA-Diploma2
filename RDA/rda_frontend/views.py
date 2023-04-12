from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm, LoginForm, NewUserProfile
from .models import Patient


# Create your views here.


def landing_page(request):
    return render(request, 'rda_frontend/my_landing.html')


def login_page(request):
    form = LoginForm()
    context = {'form': form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('../account')
        else:
            messages.info(request, 'Логин или пароль введены неверно. Повторите попытку.')
    return render(request, 'rda_frontend/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('../login')


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


def check_access_group(user):
    return user.patient.access_group.endswith('Verified')



@login_required(login_url='../login', )
def account_page(request):
    form = NewUserProfile()

    if request.method == 'POST':
        form = NewUserProfile(request.POST, instance=request.user.patient)

        if form.is_valid():
            form.save()
            Patient.objects.update(access_group='Verified')

        messages.success(request, 'Данные успешно сохранены')
        # return redirect('../login')

    context = {'form': form}
    return render(request, 'rda_frontend/account.html', context)

@login_required(login_url='../login', )
@user_passes_test(check_access_group, login_url='../account')
def edit_profile(request):
    return render(request, 'rda_frontend/edit-profile.html')

@login_required(login_url='../login', )
@user_passes_test(check_access_group, login_url='../account')
def documents_page(request):
    return render(request, 'rda_frontend/documents.html')

@login_required(login_url='../login', )
@user_passes_test(check_access_group, login_url='../account')
def analysis_page(request):
    return render(request, 'rda_frontend/analysis.html')

@login_required(login_url='../login', )
@user_passes_test(check_access_group, login_url='../account')
def add_analysis_page(request):
    return render(request, 'rda_frontend/add-analysis.html')

