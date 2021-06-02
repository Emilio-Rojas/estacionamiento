from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


from .views import *


urlpatterns = [
    path('administrar/', administrar_estacionamiento, name='administrar-estacionamiento'),
    path('privado/', estacionamiento_privado, name='estacionamiento-privado')
]