from django.contrib import admin
from .models import Administrador, Domiciliario, Vehiculo, Cliente, Pedido

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'correo', 'compania')
    search_fields = ('usuario', 'correo')


@admin.register(Domiciliario)
class DomiciliarioAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'telefono', 'estado', 'administrador')
    search_fields = ('cedula', 'nombre', 'apellido')


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'color', 'marca', 'domiciliario')
    search_fields = ('placa', 'marca')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre')
    search_fields = ('usuario', 'nombre')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'direccion_entrega', 'direccion_salida', 'precio', 'distancia', 'cliente', 'domiciliario')
    search_fields = ('direccion_entrega', 'direccion_salida')
