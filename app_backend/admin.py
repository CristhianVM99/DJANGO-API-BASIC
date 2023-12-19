from django.contrib import admin
from .models import Marca,Talla,Categoria,Color,Producto,Cargo,PersonalDeAtencion,Genero,Cliente,Pago,Venta

# Register your models here.
admin.site.register(Marca)
admin.site.register(Talla)
admin.site.register(Categoria)
admin.site.register(Color)
admin.site.register(Producto)
admin.site.register(Cargo)
admin.site.register(PersonalDeAtencion)
admin.site.register(Genero)
admin.site.register(Cliente)
admin.site.register(Pago)
admin.site.register(Venta)
