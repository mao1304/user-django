from rest_framework import serializers
from .models import Administrador, Cliente, Domiciliario, Vehiculo, Pedido

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'  # Esto incluirá todos los campos del modelo

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'  # Esto incluirá todos los campos del modelo
        
class DomiciliarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domiciliario
        fields = '__all__'  # Esto incluirá todos los campos del modelo
        
class DomiciliarioLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domiciliario
        fields = ['cedula', 'estado']
        
class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'  # Esto incluirá todos los campos del modelo
        
        
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'