from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect, render


class CustomLoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control mt-2 ', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control mt-1 ', 'placeholder': 'Password'})
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CustomLoginForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        email = self.data['email']
        password = self.data['password']
        user = authenticate(self.request, username=email, password=password)
        if user:
            login(self.request, user)
            return True
        else:
            self.add_error('email', 'Email o contraseña incorrectos')
            return False
