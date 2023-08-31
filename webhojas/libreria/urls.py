from django.urls import path
from . import views

urlpatterns= [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('ventas', views.ventas, name='ventas'),
    path('ventas/crear', views.crear_venta, name='crear'),
    path('ventas/editar', views.editar_venta, name='editar'),
    path('eliminar/<int:id>',views.eliminar,name='eliminar'),
<<<<<<< HEAD
    path('ventas/editar/<int:id>',views.editar_venta, name='editar')
]

=======
    path('login/',views.login,name='login'),
    path('registro/',views.registro,name='registro'),
    path('salir/',views.salir,name='salir'),
]
>>>>>>> 064dc6fdae03f41f7e81489ca4229d5aedbe4abc
