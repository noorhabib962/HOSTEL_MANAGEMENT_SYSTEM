from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': 'form-control', 'placeholder': 'Password' })) 
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': 'form-control', 'placeholder': 'Confirm Password' })) 
    class Meta: 
        model = User 
        fields = ('username', 'email', 'password1', 'password2') 
        widgets = { 
            'username': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Username' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control', 'placeholder': 'Email' }), 
            } 

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Username', })) 
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': 'form-control', 'placeholder': 'Password', }))
