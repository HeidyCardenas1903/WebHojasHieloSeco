from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ventas
from .forms import VentasForm
from .models import Ventas


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
    formulario = VentasForm(request.POST or None)
    if formulario.is_valid():#si el formulario es valido, se guarda el registro en la bd y se redirecciona a la seccion ventas
        formulario.save()
        return redirect('ventas')

    return render(request,'hojas/crear.html',{
        'formulario':formulario
    })

def editar_venta(request,id):
    # Funcion para editar un registro y la condicial para guardar los cambios que sean realizados 
    venta = Ventas.objects.get(id=id)
    formulario = VentasForm(request.POST or None, instance=venta) 
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('ventas')
        
    return render(request,'hojas/editar.html', {'formulario': formulario})

def eliminar(request,id):
    '''funcion para eliminar un registro'''
    venta = Ventas.objects.get(id=id) #Verifica el id del cliente para eliminar el registro y devolver a la misma seccion donde se encontraba
    venta.delete()
    return redirect('ventas')

