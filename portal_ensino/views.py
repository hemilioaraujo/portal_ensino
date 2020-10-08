from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def sobre(request):
    return render(request, 'sobre.html')
