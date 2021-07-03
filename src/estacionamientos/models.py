from django.db import models
from django.db.models.fields import related
from usuarios.models import TipoBanco, TipoCuenta, User

class TipoEstacionamiento(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.descripcion

class ComunaEstacionamiento(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.descripcion

class CategoriaEstacionamiento(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.descripcion

class EstadoEstacionamiento(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.descripcion

class Estacionamiento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_estacionamiento")
    rut = models.CharField(max_length=25, blank=False, null=True, verbose_name=u'N° documento')
    tipo_estacionamiento = models.ForeignKey(TipoEstacionamiento, on_delete=models.CASCADE, null=True, blank=True)
    comuna_estacionamiento = models.ForeignKey(ComunaEstacionamiento, on_delete=models.CASCADE, null=True, blank=True)
    categoria_estacionamiento = models.ForeignKey(CategoriaEstacionamiento, on_delete=models.CASCADE, null=True, blank=True)
    estado_estacionamiento = models.ForeignKey(EstadoEstacionamiento, on_delete=models.CASCADE, null=True, blank=True)
    calle = models.CharField(max_length=100, null=False, blank=False)
    numeracion = models.CharField(max_length=100, null=False, blank=False)
    precio_base = models.IntegerField(default=0)

    def __str__(self):
        return self.calle

class ImagenesEstacionamiento(models.Model):
    estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.estacionamiento

class Disponibilidad(models.Model):
    estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE, null=True, blank=True)
    fecha_disponibilidad = models.DateField(blank=False, null=True)
    precio_bloque = models.IntegerField(default=0)

    def __str__(self):
        return str(self.fecha_disponibilidad)

class Bloque(models.Model):
    descripcion = models.CharField(max_length=50, blank=False, null=True)

    def __str__(self):
        return self.descripcion

class BloqueDisponibilidad(models.Model):
    disponibilidad = models.ForeignKey(Disponibilidad, on_delete=models.CASCADE, null=True, blank=True, related_name ="bloque_disponibilidad")
    bloque_inicio = models.ForeignKey(Bloque, on_delete=models.CASCADE, null=True, blank=True, related_name="bloque_inicio_disponibilidad")
    bloque_termino = models.ForeignKey(Bloque, on_delete=models.CASCADE, null=True, blank=True, related_name="bloque_termino_disponibilidad")
    
    def __str__(self):
        return self.disponibilidad

class TipoReserva(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.descripcion

class TipoVehiculo(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.descripcion

class Vehiculo(models.Model):
    patente = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_vehiculo")
    rut_conductor = models.CharField(max_length=100, null=True, blank=True)
    tipo_vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.patente

class Reserva(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_reserva")
    estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE, null=True, blank=True)
    patente = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=True, blank=True)
    tipo_estacionamiento = models.ForeignKey(TipoEstacionamiento, on_delete=models.CASCADE, null=True, blank=True)
    fecha_reserva = models.DateField(blank=False, null=True, verbose_name=u'Fecha Reserva')
    bloque_inicio = models.IntegerField(null=True, blank=True)
    bloque_termino = models.IntegerField(null=True, blank=True)
    estado_reserva = models.BooleanField(default=False)

class Boleta(models.Model):
    numero_boleta = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="conductor")
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, null=True, blank=True)
    valor = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.numero_boleta

class Pago(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_pago")
    rut = models.CharField(max_length=25, blank=False, null=True, verbose_name=u'N° documento')
    tipo_banco = models.ForeignKey(TipoBanco, on_delete=models.CASCADE, null=True, blank=True, related_name="pago_tipo_banco")
    tipo_cuenta = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE, null=True, blank=True, related_name="pago_tipo_cuenta")
    numero_cuenta = models.CharField(max_length=100, null=True, blank=True)
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE, null=True, blank=True)



