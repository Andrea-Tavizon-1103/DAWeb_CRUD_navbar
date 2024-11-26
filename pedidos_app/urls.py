from django.urls import path
from pedidos_app import views  

urlpatterns = [
    path('pedido', views.inicio_vistaPedido, name='pedido'),  # La vista principal
    path('registrarPedido/', views.registrarPedido, name='registrarPedido'),
    path('borrarPedido/<idpedido>/', views.borrarPedido, name='borrarPedido'),
    path('seleccionarPedido/<idpedido>/', views.seleccionarPedido, name='seleccionarPedido'),
    path('editarPedido/', views.editarPedido, name='editarPedido')
]
