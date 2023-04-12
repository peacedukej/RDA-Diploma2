"""RDA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rda_frontend import views

#from rda_frontend.views import landing_page, login_page, logout_user, register_page, account_page, edit_profile, documents_page, analysis_page, add_analysis_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page),
    path('login/', views.login_page),
    path('logout/', views.logout_user),
    path('register/', views.register_page),
    path('account/', views.account_page),
    path('edit profile/', views.edit_profile),
    path('documents/', views.documents_page),
    path('analysis/', views.analysis_page),
    path('add analysis/', views.add_analysis_page),
]
