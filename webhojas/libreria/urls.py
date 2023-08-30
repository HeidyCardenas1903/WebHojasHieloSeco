from django.urls import path
from . import views

urlpatterns= [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('ventas', views.ventas, name='ventas'),
    path('ventas/crear', views.crear_venta, name='crear'),
    path('ventas/editar', views.editar_venta, name='editar'),
<<<<<<< HEAD
]
=======
    path('eliminar/<int:id>',views.eliminar,name='eliminar'),
]
>>>>>>> 3cfd6dbf6a3d337ad85f0c02d4f8e7c6e482be8e
