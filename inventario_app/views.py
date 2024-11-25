from django.shortcuts import render,redirect
from .models import Inventario

def inicio_vistaInventario(request):
    listaI=Inventario.objects.all()
    return render(request,'gestionarInventarios.html',{'listaInventarios':listaI})

def registrarInventario(request):
    id_inventario=  request.POST['txtinventario']
    fecha_entrada=  request.POST['txtentrada']
    estado_producto=  request.POST['txtestado']
    codigo_barras=  request.POST['txtcodigo']
    cantidad_stock=  request.POST['txtcantidad']
    descripcion=  request.POST['txtdescripcion']
    precio_unitario=  request.POST['txtprecio_unitario']
    guardarinventario=Inventario.objects.create(id_inventario=id_inventario,fecha_entrada=fecha_entrada,estado_producto=estado_producto,codigo_barras=codigo_barras,cantidad_stock=cantidad_stock,descripcion=descripcion,precio_unitario=precio_unitario)
    return redirect("inventario")

def seleccionarInventario(request,id_inventario):
    inventario = Inventario.objects.get(id_inventario=id_inventario)
    return render(request,'editarInventario.html',{'p':inventario})

def editarInventario(request):
    id_inventario=  request.POST['txtinventario']
    fecha_entrada=  request.POST['txtentrada']
    estado_producto=  request.POST['txtestado']
    codigo_barras=  request.POST['txtcodigo']
    cantidad_stock=  request.POST['txtcantidad']
    descipcion=  request.POST['txtdescripcion']
    precio_unitario=  request.POST['txtprecio_unitario']
    inventario= Inventario.objects.get(id_inventario=id_inventario)
    inventario.id_inventario =id_inventario
    inventario.fecha_entrada = fecha_entrada
    inventario.estado_producto = estado_producto
    inventario.codigo_barras = codigo_barras
    inventario.cantidad_stock = cantidad_stock
    inventario.descripcion = descipcion
    inventario.precio_unitario = precio_unitario
    inventario.save()
    return redirect("inventario")

def borrarInventario(request,id_inventario):
    inventario=Inventario.objects.get(id_inventario=id_inventario)
    inventario.delete()
    return redirect("inventario/")
# Create your views here.
