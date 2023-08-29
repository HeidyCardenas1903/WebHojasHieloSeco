from django.shortcuts import render
from django.http import HttpResponse
from .models import Ventas
# Create your views here.

def inicio(request):
    '''Funcion para el portal de inicio'''
    return render (request,'html/inicio.html' )

def nosotros(request):
    '''Funcion para el final de seccion nosotros'''
    return render (request,'html/nosotros.html' )

def ventas(request):
    ventas = Ventas.objects.all()
    print(ventas)
    return render(request,'hojas/index.html',{'ventas': ventas})

def crear_venta(request):
    '''funcion para la seccion de crear ventas'''
    return render(request,'hojas/crear.html')

def editar_venta(request):
    '''funcion para la seccion de editar ventas'''
    return render(request,'hojas/editar.html')