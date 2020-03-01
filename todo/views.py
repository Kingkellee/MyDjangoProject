from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'todo/index.html')
    

@login_required
def home(request):
    return render(request, 'todo/home.html', {'title': 'Welcome'}) 


def about(request):
    return render(request, 'todo/about.html', {'title': 'About'})