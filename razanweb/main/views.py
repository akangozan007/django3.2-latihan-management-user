from django.shortcuts import render
from django.contrib.auth.views import LoginView


# Create your views here.
def home(request):
    context = {
        'judul' : 'Beranda',
    }
    return render(request, 'main/home.html', context)

# def login(request):
#     context = {
#         'judul' : 'Laman Login',
#     }
#     return render(request, 'registration/login.html', context)
def login(request):

    class CustomLoginView(LoginView):
        template_name = 'registration/login.html'
        redirect_authenticated_user = True

    return render(request, 'registration/login.html')