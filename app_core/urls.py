from django.urls import path
from .views import AdministradorListCreateView, AdministradorDetailView, ClienteListCreateView, ClienteDetailView,DomiciliarioListCreateView, DomiciliarioDetailView, VehiculoListCreateView, VehiculoDetailView, PedidoListCreateView, PedidoDetailView, login_admin, login_cliente, login_domiciliario, logout_user

urlpatterns = [
    # Ruta para crear y listar administradores
    path('admin/', AdministradorListCreateView.as_view(), name='administrador-list-create'),
    # Ruta para obtener, actualizar y eliminar un administrador específico
    path('admin/<str:pk>/', AdministradorDetailView.as_view(), name='administrador-detail'),
    path('client/', ClienteListCreateView.as_view(), name='administrador-list-create'),
    # Ruta para obtener, actualizar y eliminar un administrador específico
    path('client/<str:pk>/', ClienteDetailView.as_view(), name='administrador-detail'),
    path('domi/', DomiciliarioListCreateView.as_view(), name='administrador-list-create'),
    # Ruta para obtener, actualizar y eliminar un administrador específico
    path('domi/<str:pk>/', DomiciliarioDetailView.as_view(), name='administrador-detail'),
    # Ruta para crear y listar vehiculos
    path('vehiculo/', VehiculoListCreateView.as_view(), name='vehiculo-list-create'),
    # Ruta para obtener, actualizar y eliminar un vehiculo específico
    path('vehiculo/<str:pk>/', VehiculoDetailView.as_view(), name='vehiculo-detail'),
    # Ruta para crear y listar pedidos
    path('pedido/', PedidoListCreateView.as_view(), name='pedido-list-create'),
    # Ruta para obtener, actualizar y eliminar un pedido específico
    path('pedido/<str:pk>/', PedidoDetailView.as_view(), name='pedido-detail'),
    #crear rutas para las vistas de login y logout
    path('login_admin/', login_admin, name='login_admin'),
    path('login_cliente/', login_cliente, name='login_cliente'),    
    path('login_domiciliario/', login_domiciliario, name='login_domiciliario'),
    path('logout/', logout_user, name='logout'),
]   
