from django.contrib import admin

from pedidos.models import Clientes, Productos, Pedidos

# Register your models here.
admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Pedidos)