from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")