from django.urls import path
from . import views

urlpatterns= [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('ventas', views.ventas, name='ventas'),
    path('ventas/crear', views.crear_venta, name='crear'),
]