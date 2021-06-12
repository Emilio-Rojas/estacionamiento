from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


from .views import *


urlpatterns = [
  path('disponibilidad/', disponibilidad_estacionamiento, name='disponibilidad-estacionamiento'),
 
  #Estacionamiento particulares
  path('particular/', include([
      path('agregar/', estacionamiento_particular_agregar, name='estacionamiento-particular-agregar'),
      path('listar/', estacionamiento_particular_listar, name='estacionamiento-particular-listar'),
      path('editar/<int:id_estacionamiento>/', estacionamiento_particular_editar, name='estacionamiento-particular-editar'),
      path('eliminar/<int:id_estacionamiento>/', estacionamiento_particular_eliminar, name='estacionamiento-particular-eliminar')
    ])),

  #Disponibilidad de estacionamientos (Vista arrendador)
  path('disponibilidad/', include([
      path('<int:id_estacionamiento>/', estacionamiento_disponibilidad_detalle, name='disponibilidad-detalle'),  
      path('<int:id_estacionamiento>/agregar/', estacionamiento_disponibilidad_agregar, name='disponibilidad-agregar'), 
      path('<int:id_estacionamiento>/editar/<int:id_disponibilidad>', estacionamiento_disponibilidad_editar, name='disponibilidad-editar'),
      path('<int:id_estacionamiento>/eliminar/<int:id_disponibilidad>', estacionamiento_disponibilidad_eliminar, name='disponibilidad-eliminar')
  ])),

  #Estacionamiento privados
  path('privado/', include([
      path('agregar/', estacionamiento_privado_agregar, name='estacionamiento-privado-agregar'),
      path('listar/', estacionamiento_privado_listar, name='estacionamiento-privado-listar'),
      path('editar/<int:id_estacionamiento>/', estacionamiento_privado_editar, name='estacionamiento-privado-editar'),
      path('eliminar/<int:id_estacionamiento>/', estacionamiento_privado_eliminar, name='estacionamiento-privado-eliminar')
    ])),

]