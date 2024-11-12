from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Administrador, Domiciliario, Cliente, Vehiculo, Pedido
from .serializers import AdministradorSerializer, DomiciliarioSerializer, ClienteSerializer, DomiciliarioLogSerializer, VehiculoSerializer, PedidoSerializer
import requests

# Crear y listar administradores
class AdministradorListCreateView(generics.ListCreateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

# Detalle, actualización y eliminación de un administrador específico
class AdministradorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    
#crear y listar clientes
class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

#detalle, actualización y eliminación de un cliente específico
class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
#crear y listar domiciliarios
class DomiciliarioListCreateView(generics.ListCreateAPIView):
    queryset = Domiciliario.objects.all()    
    serializer_class = DomiciliarioSerializer    

#detalle, actualización y eliminación de un domiciliario específico
class DomiciliarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Domiciliario.objects.all()
    serializer_class = DomiciliarioSerializer   

#crear y listar vehiculos
class VehiculoListCreateView(generics.ListCreateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

#detalle, actualización y eliminación de un vehiculo específico
class VehiculoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehiculo.objects.all()    
    serializer_class = VehiculoSerializer
    
#crear y listar pedidos
class PedidoListCreateView(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def perform_create(self, serializer):
        # Obtener la dirección de salida y entrega del nuevo pedido
        direccion_salida = self.request.data.get('direccion_salida')
        direccion_entrega = self.request.data.get('direccion_entrega')

        # Dividir la cadena en latitud y longitud y convertir a float
        try:
            salida_lat, salida_lng = map(float, direccion_salida.split(','))
            entrega_lat, entrega_lng = map(float, direccion_entrega.split(','))
        except (ValueError, AttributeError):
            raise ValueError("Las direcciones deben estar en formato de coordenadas, e.g., 'latitud,longitud'")

        # Usar las coordenadas convertidas en la solicitud a la API
        url = "https://graphhopper.com/api/1/route"
        
        # Crear un diccionario con todos los parámetros necesarios
        params = {
            "profile": "bike",
            "locale": "en",
            "instructions": "true",
            "calc_points": "true",
            "debug": "false",
            "points_encoded": "true",
            "key": "eb8e5296-c15d-400b-b969-d7cb6b51bd8b",
            "point": [f"{salida_lat},{salida_lng}", f"{entrega_lat},{entrega_lng}"]
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            # Extraer la distancia del resultado de la API
            distancia_total = data['paths'][0]['distance']
            # Guardar el pedido con la distancia obtenida
            price=round((distancia_total*1.5), -2)
            serializer.save(distancia=distancia_total)
            serializer.save(precio=price)
        else:
            print(f"Error en la API de Graphhopper: {response.status_code} - {response.text}")
            raise ValueError("Error en la solicitud de distancia a la API de Graphhopper")
#detalle, actualización y eliminación de un pedido específico
class PedidoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()    
    serializer_class = PedidoSerializer
# Función auxiliar para autenticación
def authenticate_user(model, lookup_field, identifier, password):
    try:
        print(f"datos::::{model} {lookup_field}, {identifier}, {password}")
        user = model.objects.get(**{lookup_field: identifier})
        print(user)
    except model.DoesNotExist:
        return None, "Usuario no encontrado"

    if user.check_password(password):
        return user, None
    else:
        return None, "Contraseña incorrecta"


# Vista para login de Administrador
@api_view(['POST'])
def login_admin(request):
    usuario = request.data.get("usuario")
    password = request.data.get("password")
    print(password)
    print(usuario)
    
    administrador, error = authenticate_user(Administrador, "usuario", usuario, password)
    
    if administrador:
        return Response({"detail": "Login con exitoso", "usuario": administrador.usuario}, status=status.HTTP_200_OK)
    else:
        return Response({"detail": error}, status=status.HTTP_401_UNAUTHORIZED)


# Vista para login de Domiciliario
@api_view(['POST'])
def login_domiciliario(request):
    cedula = request.data.get("cedula")
    password = request.data.get("password")
    domiciliario, error = authenticate_user(Domiciliario, "cedula", cedula, password)
    if domiciliario:
        return Response({"detail": "Login exitoso", "usuario": domiciliario.cedula, "estado": domiciliario.estado }, status=status.HTTP_200_OK)
    else:
        return Response({"detail": error}, status=status.HTTP_401_UNAUTHORIZED)


# Vista para login de Cliente
@api_view(['POST'])
def login_cliente(request):
    usuario = request.data.get("usuario")
    password = request.data.get("password")
    cliente, error = authenticate_user(Cliente, "usuario", usuario, password)
    
    if cliente:
        return Response({"detail": "Login exitoso", "usuario": cliente.usuario}, status=status.HTTP_200_OK)
    else:
        return Response({"detail": error}, status=status.HTTP_401_UNAUTHORIZED)


# Vista para cerrar sesión
@api_view(['POST'])
def logout_user(request):
    logout(request)
    return Response({"detail": "Logout exitoso"}, status=status.HTTP_200_OK)
