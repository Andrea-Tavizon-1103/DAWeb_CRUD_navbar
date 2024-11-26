from django.db import models

# Create your models here.

class Proveedor(models.Model):
    idproveedor=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=100)
    contacto=models.CharField(max_length=100)
    correo=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    direccion=models.CharField(max_length=100)
    fecha_registro=models.DateField()

    def __str__(self) :
        return self.nombre 
