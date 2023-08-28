from django.urls import path
from . import wiews

urlpatterns= [
    path('', views.index, name='index'),
]