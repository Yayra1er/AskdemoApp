from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')


def apropos(request):
    return render(request, 'apropos.html')


def solution(request):
    return  render(request, 'solution.html')


def offre(request):
    return render(request, 'offre.html')


def contact(request):
    return render(request, 'contact.html')