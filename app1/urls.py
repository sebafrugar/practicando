from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('main_register', views.main_register),
    path('main_logeado', views.main_logeado),
    path('crear_comentario', views.main_logeado),
 
]
