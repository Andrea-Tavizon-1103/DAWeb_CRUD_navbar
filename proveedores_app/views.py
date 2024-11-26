from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor

def inicio_vistaProveedor(request):
    losproveedores = Proveedor.objects.all()
    return render(request, "gestionarProveedor.html", {"misproveedores": losproveedores})

def registrarProveedor(request):
    idproveedor = request.POST["txtidproveedor"]
    nombre = request.POST["txtnombre"]
    contacto = request.POST["txtcontacto"]
    correo = request.POST["txtcorreo"]
    telefono = request.POST["numtelefono"]
    direccion = request.POST["txtdireccion"]
    fecha_registro = request.POST["txtfecharegistro"]

    Proveedor.objects.create(
        idproveedor=idproveedor,
        nombre=nombre,
        contacto=contacto,
        correo=correo,
        telefono=telefono,
        direccion=direccion,
        fecha_registro=fecha_registro,
    )
    return redirect("proveedor")

def borrarProveedor(request, idproveedor):
    proveedor = get_object_or_404(Proveedor, idproveedor=idproveedor)
    proveedor.delete()
    return redirect("proveedor")

def seleccionarProveedor(request, idproveedor):
    proveedor = get_object_or_404(Proveedor, idproveedor=idproveedor)
    return render(request, "editarProveedor.html", {"proveedor": proveedor})

def editarProveedor(request):
    idproveedor = request.POST["txtidproveedor"]
    nombre = request.POST["txtnombre"]
    contacto = request.POST["txtcontacto"]
    correo = request.POST["txtcorreo"]
    telefono = request.POST["numtelefono"]
    direccion = request.POST["txtdireccion"]
    fecha_registro = request.POST["txtfecharegistro"]

    proveedor = get_object_or_404(Proveedor, idproveedor=idproveedor)

    proveedor.nombre = nombre
    proveedor.contacto = contacto
    proveedor.correo = correo
    proveedor.telefono = telefono
    proveedor.direccion = direccion
    proveedor.fecha_registro = fecha_registro
    proveedor.save()

    return redirect("proveedor")
