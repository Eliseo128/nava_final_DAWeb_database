from django.shortcuts import render,redirect
from .models import Proveedores

def inicio_vista(request):
    listaProv=Proveedores.objects.all()
    return render(request,'gestionarProveedores.html',{'listaProveedores':listaProv})

def registrarProveedores(request):
    id_proveedor=  request.POST['txtproveedor']
    nombre=  request.POST['txtnombre']
    edad=  request.POST['txtedad']
    tipo_producto=  request.POST['txttipo_proveedor']
    horario=  request.POST['txthorario']
    telefono=  request.POST['txttelefono']
    direccion=  request.POST['txtdireccion']
    guardarproveedor=Proveedores.objects.create(id_proveedor=id_proveedor,nombre=nombre,edad=edad,tipo_producto=tipo_producto,horario=horario,telefono=telefono,direccion=direccion)
    return redirect("/")

def seleccionarProveedor(request,id_proveedor):
    proveedor = Proveedores.objects.get(id_proveedor=id_proveedor)
    return render(request,'editarProveedor.html',{'c':proveedor})

def editarProveedor(request):
    id_proveedor=  request.POST['txtproveedor']
    nombre=  request.POST['txtnombre']
    edad=  request.POST['txtedad']
    tipo_producto=  request.POST['txttipo_proveedor']
    horario=  request.POST['txthorario']
    telefono=  request.POST['txttelefono']
    direccion=  request.POST['txtdireccion']
    proveedor= Proveedores.objects.get(id_proveedor=id_proveedor)
    proveedor.id_proveedor =id_proveedor
    proveedor.nombre = nombre
    proveedor.edad = edad
    proveedor.tipo_producto=tipo_producto
    proveedor.horario = horario
    proveedor.telefono = telefono
    proveedor.direccion = direccion
    proveedor.save()
    return redirect("/")

def borrarProveedor(request,id_proveedor):
    proveedor=Proveedores.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()
    return redirect("/")
# Create your views here.


