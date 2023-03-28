from django.shortcuts import render


# Create your views here.

def landing_page(request):
    return render(request, 'rda_frontend/my_landing.html')


def login_page(request):
    return render(request, 'rda_frontend/login.html')


def register_page(request):
    return render(request, 'rda_frontend/register.html')


def account_page(request):
    return render(request, 'rda_frontend/account.html')


def edit_profile(request):
    return render(request, 'rda_frontend/edit-profile.html')


def documents_page(request):
    return render(request, 'rda_frontend/documents.html')


def add_analysis_page(request):
    return render(request, 'rda_frontend/add-analysis.html')
