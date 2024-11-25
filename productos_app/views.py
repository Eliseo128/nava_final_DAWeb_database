from django.shortcuts import render,redirect
from .models import Productos

def inicio_vista(request):
    listaP=Productos.objects.all()
    return render(request,'gestionarProductos.html',{'listaProductos':listaP})

def registrarProducto(request):
    id_producto=  request.POST['txtproducto']
    precio=  request.POST['txtprecio']
    marca=  request.POST['txtmarca']
    nombre=  request.POST['txtnombre']
    categoria=  request.POST['txtcategoria']
    diseño=  request.POST['txtdiseño']
    calidad=  request.POST['txtcalidad']
    guardarproducto=Productos.objects.create(id_producto=id_producto,precio=precio,marca=marca,nombre=nombre,categoria=categoria,diseño=diseño,calidad=calidad)
    return redirect("/")

def seleccionarProducto(request,id_producto):
    producto = Productos.objects.get(id_producto=id_producto)
    return render(request,'editarProducto.html',{'p':producto})

def editarProducto(request):
    id_producto=  request.POST['txtproducto']
    precio=  request.POST['txtprecio']
    marca=  request.POST['txtmarca']
    nombre=  request.POST['txtnombre']
    categoria=  request.POST['txtcategoria']
    diseño=  request.POST['txtdiseño']
    calidad=  request.POST['txtcalidad']
    producto= Productos.objects.get(id_producto=id_producto)
    producto.id_producto =id_producto
    producto.precio = precio
    producto.marca = marca
    producto.nombre = nombre
    producto.categoria = categoria
    producto.diseño = diseño
    producto.calidad = calidad
    producto.save()
    return redirect("/")

def borrarProducto(request,id_producto):
    producto=Productos.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect("/")
# Create your views here.
