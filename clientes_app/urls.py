from django.urls import path
from clientes_app import views  

urlpatterns = [
    path('cliente', views.inicio_vistaCliente, name='cliente'),  # La vista principal
    path('registrarCliente/', views.registrarCliente, name='registrarCliente'),
    path('borrarCliente/<ID_Cliente>/', views.borrarCliente, name='borrarCliente'),
    path('seleccionarCliente/<ID_Cliente>/', views.seleccionarCliente, name='seleccionarCliente'),
    path('editarCliente/', views.editarCliente, name='editarCliente')
]
