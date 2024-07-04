from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'judul' : 'Beranda',
    }
    return render(request, 'main/home.html', context)


