from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterForm

# Create your views here.

def landing_page(request):
    return render(request, 'rda_frontend/my_landing.html')


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

    context = {'form': form}
    return render(request, 'rda_frontend/register.html', context)


def account_page(request):
    return render(request, 'rda_frontend/account.html')


def edit_profile(request):
    return render(request, 'rda_frontend/edit-profile.html')


def documents_page(request):
    return render(request, 'rda_frontend/documents.html')


def analysis_page(request):
    return render(request, 'rda_frontend/analysis.html')


def add_analysis_page(request):
    return render(request, 'rda_frontend/add-analysis.html')