# from django.conf.urls import url
from django.urls import path
from django.contrib import admin
# memanggil segugusan function views didalam main app views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/home', views.home, name='home'),
    # path('login/', views_login.login, name='login')
]