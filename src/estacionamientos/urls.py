from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


from .views import *


urlpatterns = [
 
   #Estacionamiento particulares
    path('particular/', include([
        path('agregar/', estacionamiento_particular_agregar, name='estacionamiento-particular-agregar'),
        path('listar/', estacionamiento_particular_listar, name='estacionamiento-particular-listar'),
        path('editar/<int:id_estacionamiento>/', estacionamiento_particular_editar, name='estacionamiento-particular-editar'),
        path('eliminar/<int:id_estacionamiento>/', estacionamiento_particular_eliminar, name='estacionamiento-particular-eliminar')


      ])),

    #Estacionamiento privados

    path('privado/', include([
        path('agregar/', estacionamiento_privado_agregar, name='estacionamiento-privado-agregar'),
        path('listar/', estacionamiento_privado_disponibilidad, name='estacionamiento-privado-disponibilidad'),
        path('editar/<int:id_estacionamiento>/', estacionamiento_privado_editar, name='estacionamiento-privado-editar'),
        path('eliminar/<int:id_estacionamiento>/', estacionamiento_privado_eliminar, name='estacionamiento-privado-eliminar')


      ])),

]