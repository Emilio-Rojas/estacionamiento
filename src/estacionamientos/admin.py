from django.contrib import admin
from .models import Bloque, TipoEstacionamiento, ComunaEstacionamiento, CategoriaEstacionamiento, Estacionamiento, TipoReserva, TipoVehiculo
from .models import Vehiculo, Reserva, EstadoEstacionamiento, BloqueDisponibilidad

# Register your models here.
admin.site.register(TipoEstacionamiento)
admin.site.register(ComunaEstacionamiento)
admin.site.register(CategoriaEstacionamiento)
admin.site.register(Estacionamiento)
admin.site.register(TipoReserva)
admin.site.register(TipoVehiculo)
admin.site.register(Vehiculo)
admin.site.register(Reserva)
admin.site.register(Bloque)
admin.site.register(EstadoEstacionamiento)
admin.site.register(BloqueDisponibilidad)
