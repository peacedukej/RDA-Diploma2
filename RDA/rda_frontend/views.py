from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate, get_user_model
from .forms import *


def landing_page(request):
    # if 'user_id' in request.session:
    #     user = get_user(request)
    #     # return render(request, 'rda_frontend/my_landing.html')
    #     return render(request, '../my_landing', {'user': user})
    # else:
    #     return redirect('../login')
    return render(request, 'rda_frontend/my_landing.html')

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