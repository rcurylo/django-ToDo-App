from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#uses bootstrap and django-crispy-forms
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    #change some of the properties of the parent form
    class Meta:
        model = User
        fields=["username","email","password1","password2"]