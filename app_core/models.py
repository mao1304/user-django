from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Modelo de Administrador
class Administrador(models.Model):
    usuario = models.CharField(max_length=50, primary_key=True, unique=True)
    password = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True)
    compania = models.CharField(max_length=100)

    def set_password(self, password):
        self.password = make_password(password)

    def check_password(self, password):
        # Verifica si la contraseña ingresada coincide con la almacenada
        return self.password == password

    def __str__(self):
        return self.usuario


# Modelo de Domiciliario
class Domiciliario(models.Model):
    cedula = models.CharField(max_length=20, primary_key=True, unique=True)
    password = models.CharField(max_length=100)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    estado = models.CharField(max_length=50)
    administrador = models.ForeignKey(Administrador, related_name='domiciliarios', on_delete=models.CASCADE)

    def set_password(self, password):
        self.password = make_password(password)

    def check_password(self, password):
        # Verifica si la contraseña ingresada coincide con la almacenada
        return self.password == password

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.cedula})'


# Modelo de Cliente
class Cliente(models.Model):
    usuario = models.CharField(max_length=50, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def set_password(self, password):
        self.password = make_password(password)

    def check_password(self, password):
        # Verifica si la contraseña ingresada coincide con la almacenada
        return self.password == password

    def __str__(self):
        return self.usuario


# Modelo de Vehículo
class Vehiculo(models.Model):
    placa = models.CharField(max_length=20, primary_key=True, unique=True)
    color = models.CharField(max_length=30)
    marca = models.CharField(max_length=50)
    domiciliario = models.ForeignKey(Domiciliario, related_name='vehiculos', on_delete=models.CASCADE)

    def __str__(self):
        return self.placa
# Modelo de Pedido
class Pedido(models.Model):
    direccion_entrega = models.CharField(max_length=255,)
    direccion_salida = models.CharField(max_length=255)
    precio = models.FloatField( null=True)
    distancia = models.FloatField( null=True)
    estado = models.CharField( max_length=100, default='Pendiente', blank=True)
    cliente = models.ForeignKey(Cliente, related_name='pedidos', on_delete=models.CASCADE, null=True)
    domiciliario = models.ForeignKey(Domiciliario, related_name='pedidos', on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return f'Pedido {self.id} - {self.direccion_entrega}'
