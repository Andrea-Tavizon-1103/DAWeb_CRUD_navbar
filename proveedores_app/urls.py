from django.urls import path
from proveedores_app import views  

urlpatterns = [
    path('proveedor', views.inicio_vistaProveedor, name='proveedor'),  # La vista principal
    path('registrarProveedor/', views.registrarProveedor, name='registrarProveedor'),
    path('borrarProveedor/<idproveedor>/', views.borrarProveedor, name='borrarProveedor'),
    path('seleccionarProveedor/<idproveedor>/', views.seleccionarProveedor, name='seleccionarProveedor'),
    path('editarProveedor/', views.editarProveedor, name='editarProveedor')
]
