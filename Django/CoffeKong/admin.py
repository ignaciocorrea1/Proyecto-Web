from django.contrib import admin
from .models import cliente, vendedor, tarjeta, tipoProducto, producto, pedido, detallePedido

# Register your models here.
admin.site.register(cliente)
admin.site.register(vendedor)
admin.site.register(tarjeta)
admin.site.register(tipoProducto)
admin.site.register(producto)
admin.site.register(pedido)
admin.site.register(detallePedido)