from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class TipoUsuario(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.descripcion

class ComunasUsuario(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.descripcion

class User(AbstractUser):
    class Gender(models.IntegerChoices):
        MALE = 0, 'Masculino'
        FEMALE = 1, 'Femenino'
        OTHER = 2, 'Otro'

    username = None
    email = models.EmailField('email address', unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    rut = models.CharField(max_length=25, blank=False, null=True, verbose_name=u'N° documento')
    gender = models.IntegerField(choices=Gender.choices, blank=False, null=True, default=Gender.OTHER)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, null=True, blank=True, related_name="usuario_tipo")
    comuna_usuario = models.ForeignKey(ComunasUsuario, on_delete=models.CASCADE, null=True, blank=True, related_name="usuario_comuna")
    birth_date = models.DateField(blank=False, null=True, verbose_name=u'Fecha de Nacimiento')
    razon_social = models.CharField(max_length=60, blank=True, null=True, verbose_name=u'Razon Social')
    nombres_representante = models.CharField(max_length=80, blank=True, null=True, verbose_name=u'Nombres Representante')
    apellido_pat_representante =  models.CharField(max_length=80, blank=True, null=True, verbose_name=u'Apellido Paterno Representante')
    apellido_mat_representante =  models.CharField(max_length=80, blank=True, null=True, verbose_name=u'Apellido materno Representante')
    direccion =  models.CharField(max_length=100, blank=True, null=True, verbose_name=u'Dirección')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class TipoBanco(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.descripcion

class TipoCuenta(models.Model):
    descripcion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.descripcion

class Deposito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="usuario_deposito")
    rut = models.CharField(max_length=25, blank=False, null=True, verbose_name=u'N° documento')
    tipo_banco = models.ForeignKey(TipoBanco, on_delete=models.CASCADE, null=True, blank=True, related_name="banco_tipo")
    tipo_cuenta = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE, null=True, blank=True, related_name="cuenta_tipo")
    numero_cuenta = models.CharField(max_length=100, null=True, blank=True)
    correo_comprobante = models.CharField(max_length=100, null=True, blank=True)



