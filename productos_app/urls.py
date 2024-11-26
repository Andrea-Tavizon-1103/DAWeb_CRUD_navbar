from django.urls import path
from productos_app import views  

urlpatterns = [
    path('producto', views.inicio_vistaProducto, name='producto'),  
    path('registrarProducto/', views.registrarProducto, name='registrarProducto'),
    path('borrarProducto/<idproducto>/', views.borrarProducto, name='borrarProducto'),
    path('seleccionarProducto/<idproducto>/', views.seleccionarProducto, name='seleccionarProducto'),
    path('editarProducto/', views.editarProducto, name='editarProducto')
]
