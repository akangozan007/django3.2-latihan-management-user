from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
class FormPendaftaran(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# class form post

class PostinganForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","description"]