from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Ventas
from .forms import VentasForm
from django.contrib import auth
from django.contrib.auth import login as lg
from django.contrib.auth import authenticate
from django.contrib import messages 
from django.contrib.auth import logout
from .forms import Registro
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    '''Función que controla el login del usuario'''
    if request.user.is_authenticated:#si el usuario ya esta autenticado evita que pueda acceder a la pagina de logeo
        return redirect('inicio')
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuarios = authenticate(username=username, password=password)
        if usuarios:
            lg(request,usuarios)
            messages.success(request,f'Bienvenido {usuarios.username}')
            #Si es usuario es autenticado correctamente, se le redireccionara a la pagina principal de la tienda, con el mensaje de bienvenida
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])#lo va a llevar a donde el usuario previamente quiso entrar
            return redirect('ventas')
        
        else:
            messages.error(request,'Usuario y/o contraseña incorrecto')
        
    return render(request, 'html/login.html',{})

def salir(request):
    '''Funcion para cerrar sesion del usuario'''
    logout(request)
    messages.success(request,'Sesión Finalizada')#Una vez finalice la sesion se redirigira al login con el respectivo mensaje
    return redirect(login)

def registro(request):
    '''funcion que incluye el formulario de registro de un nuevo cliente'''
    if request.user.is_authenticated:#si el usuario ya esta autenticado evita que pueda acceder a la pagina de registro
        return redirect('inicio')

    form = Registro(request.POST or None) #Almacena lo que hay en la clase Registro del archivo forms
    if request.method=='POST' and form.is_valid():
       
       username = form.cleaned_data.get('username') 
       password = form.cleaned_data.get('password')
       email = form.cleaned_data.get('email')


       usuario = User.objects.create_user(username,email,password) #almacena las variables creadas anteriormente con el metodo User
       usuario.save()

       if usuario:
           #Si el usuario es creado correctamente se redirecciona a la pagina principal de la tienda
           lg(request,usuario)
           messages.success(request,f'Bienvenido {username}')
           return redirect('inicio')

    return render(request,'html/registro.html',{
        'form':form
    })


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

def editar_venta(request):
    '''funcion para la seccion de editar ventas'''
    return render(request,'hojas/editar.html')


def eliminar(request,id):
    '''funcion para eliminar un registro'''
    venta = Ventas.objects.get(id=id) #Verifica el id del cliente para eliminar el registro y devolver a la misma seccion donde se encontraba
    venta.delete()
    return redirect('ventas')



