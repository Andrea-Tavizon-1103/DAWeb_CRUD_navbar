from django.urls import path
from empleados_app import views  

urlpatterns = [
    path('empleado', views.inicio_vistaEmpleado, name='empleado'),  # La vista principal
    path('registrarEmpleado/', views.registrarEmpleado, name='registrarEmpleado'),
    path('borrarEmpleado/<idempleado>/', views.borrarEmpleado, name='borrarEmpleado'),
    path('seleccionarEmpleado/<idempleado>/', views.seleccionarEmpleado, name='seleccionarEmpleado'),
    path('editarEmpleado/', views.editarEmpleado, name='editarEmpleado')
]
