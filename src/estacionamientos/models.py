from django.db import models
from usuarios.models import User

class TipoEstacionamiento(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)

class ComunaEstacionamiento(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)

class CategoriaEstacionamiento(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)

class Estacionamiento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_estacionamiento")
    rut = models.CharField(max_length=25, blank=False, null=True, verbose_name=u'N° documento')
    tipo_estacionamiento = models.ForeignKey(TipoEstacionamiento, on_delete=models.CASCADE, null=True, blank=True)
    comuna_estacionamiento = models.ForeignKey(ComunaEstacionamiento, on_delete=models.CASCADE, null=True, blank=True)
    categoria_estacionamiento = models.ForeignKey(CategoriaEstacionamiento, on_delete=models.CASCADE, null=True, blank=True)
    calle = models.CharField(max_length=100, null=False, blank=False)
    numeracion = models.CharField(max_length=100, null=False, blank=False)

class TipoReserva(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)

class TipoVehiculo(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)

class Vehiculo(models.Model):
    patente = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_vehiculo")
    rut_conductor = models.CharField(max_length=100, null=True, blank=True)
    tipo_vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE, null=True, blank=True)

class Reserva(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_reserva")
    estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE, null=True, blank=True)
    patente = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=True, blank=True)
    tipo_estacionamiento = models.ForeignKey(TipoEstacionamiento, on_delete=models.CASCADE, null=True, blank=True)
    fecha_reserva = models.DateField(blank=False, null=True, verbose_name=u'Fecha Reserva')
    bloque_inicio = models.IntegerField(null=True, blank=True)
    bloque_termino = models.IntegerField(null=True, blank=True)
    estado_reserva = models.BooleanField(default=False)

class EstadoEstacionamiento(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)

class BloqueDisponibilidad(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)

