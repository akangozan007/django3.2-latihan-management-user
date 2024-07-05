from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'judul' : 'Beranda',
    }
    return render(request, 'main/home.html', context)

def login(request):
    context = {
        'judul' : 'Laman Login',
    }
    return render(request, 'registration/login.html', context)


