from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout as auth_logout
from django.conf import settings
from django.http import HttpResponse

# import forms pendaftaran
from .forms import FormPendaftaran
# Create your views here.
from django.contrib.auth import login as auth_login, logout, authenticate

def home(request):
    context = {
        'judul': 'Beranda',
    }
    return render(request, 'main/home.html', context)

def login(request):
    class CustomLoginView(LoginView):
        template_name = 'registration/login.html'
        redirect_authenticated_user = True
        
        def get(self, request, *args, **kwargs):
            return render(request, self.template_name)

    return CustomLoginView.as_view()(request)

def dashboard(request):
    context = {
        'judul': 'Dashboard',
    }
    return render(request, 'main/dashboard.html', context)

def Logout(request):
    auth_logout(request)
    return redirect('/login')

def daftar(request):
    context = {
        'judul': 'Form Pendaftaran',
    }
    if request.method == 'POST':
        form = FormPendaftaran(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/dashboard')
    else:
        form = FormPendaftaran()
    
    return render(request, 'registration/daftar.html', {'form': form})
