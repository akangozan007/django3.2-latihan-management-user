# from django.conf.urls import url
from django.urls import path, re_path

from django.contrib.auth import views as auth_views

from django.contrib import admin
# from django.contrib.auth.views import *
from django.conf.urls import url
# import django.contrib.auth
# memanggil segugusan function views didalam main app views
# from .views import CustomLoginView
from . import views as views_main


urlpatterns = [
    path('', views_main.home, name='home'),
    path('home/', views_main.home, name='home'),
    path('login/', views_main.LoginView.as_view(), name='login'),
    path('dashboard/', views_main.dashboard, name='dashboard'),
    path('logout/', views_main.Logout, name='Logout'),
    path('daftar/', views_main.daftar, name='daftar'),
 
]

