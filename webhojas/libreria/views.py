from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render (request,'html/inicio.html' )

def nosotros(request):
    return render (request,'html/nosotros.html' )

def ventas(request):
    return render(request,'hojas/index.html' )

def crear_venta(request):
    return render(request,'hojas/crear.html')

def editar_venta(request):
    return render(request,'hojas/editar.html')