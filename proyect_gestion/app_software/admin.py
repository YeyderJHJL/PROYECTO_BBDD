from django.contrib import admin

# Register your models here.

from .models import *
# Register your models here.
admin.site.register(Cliente)
admin.site.register(TipoCliente)
admin.site.register(EstadoCliente)
admin.site.register(EstadoRegistro)

