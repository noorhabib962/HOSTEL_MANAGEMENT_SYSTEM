from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return HttpResponse('Hello')
@login_required
def dashboard(request):
    return render(request,'dashboard/home.html')