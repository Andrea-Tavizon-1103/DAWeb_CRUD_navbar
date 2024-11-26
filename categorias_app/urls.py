from django.urls import path
from categorias_app import views

urlpatterns = [
    path('categoria', views.inicio_vistaCategoria, name='categoria'),  # La vista principal
    path('registrarCategoria/', views.registrarCategoria, name='registrarCategoria'),
    path('borrarCategoria/<idcategoria>/', views.borrarCategoria, name='borrarCategoria'),
    path('seleccionarCategoria/<idcategoria>/', views.seleccionarCategoria, name='seleccionarCategoria'),
    path('editarCategoria/', views.editarCategoria, name='editarCategoria')
]
