from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


from .views import *


urlpatterns = [
    path('administrar/', administrar_estacionamiento, name='administrar-estacionamiento'),
    path('disponibilidad/', disponibilidad_estacionamiento, name='disponibilidad-estacionamiento'),
    path('privado/', estacionamiento_privado, name='estacionamiento-privado'),

    #Estacionamiento particulares
    path('particular/', include([
        path('agregar/', estacionamiento_particular_agregar, name='estacionamiento-particular-agregar'),
        path('listar/', estacionamiento_particular_listar, name='estacionamiento-particular-listar'),
        path('editar/<int:id_estacionamiento>/', estacionamiento_particular_editar, name='estacionamiento-particular-editar'),
        path('eliminar/<int:id_estacionamiento>/', estacionamiento_particular_eliminar, name='estacionamiento-particular-eliminar')
    ])),
]