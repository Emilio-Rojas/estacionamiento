from django.contrib import admin
from .models import TipoUsuario, ComunasUsuario, User, TipoBanco, TipoCuenta, Deposito

# Register your models here.
admin.site.register(TipoUsuario)
admin.site.register(ComunasUsuario)
admin.site.register(User)
admin.site.register(TipoBanco)
admin.site.register(TipoCuenta)
admin.site.register(Deposito)