from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def incio(request):
    return HttpResponse("<h1>Bienvenido<h1>")