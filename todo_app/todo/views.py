from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'todo/index.html')


def home(request):
    return render(request, 'todo/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'todo/about.html', {'title': 'About'})