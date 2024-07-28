from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout as auth_logout
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from .forms import FormPendaftaran, PostinganForm
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post
import json


def home(request):
    context = {
        'judul': 'Beranda',
    }
    return render(request, 'main/home.html', context)

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


def login(request):
    return CustomLoginView.as_view()(request)

@login_required(login_url="/login/")
def dashboard(request):
    posts = Post.objects.all()
    context = {
        'judul': 'Dashboard',
    }
    
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
            context['respon'] = post_id
            print(post_id)
    
    context['posts'] = posts
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
    
    return render(request, 'registration/daftar.html', {'form': form, 'judul': 'Form Pendaftaran'})

# membuat postingan

@login_required(login_url="/login/")
def buat_posting(request):
    if request.method == 'POST':
        form = PostinganForm(request.POST)
        if form.is_valid():
            # secara default form.save(commit=True)
            # ini agar melarang user sembarang mengcommit
            post = form.save(commit=False)
            post.author = request.user
            # menyimpan postingan ke dalam database
            post.save()
            return redirect('/dashboard')  # Mengarahkan pengguna ke dashboard setelah postingan berhasil dibuat
    else:
        form = PostinganForm()

    return render(request, 'main/buatposting.html', {"form": form})
          
        

