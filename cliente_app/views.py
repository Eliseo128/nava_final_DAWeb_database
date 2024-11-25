from django.shortcuts import render,redirect
from .models import Cliente

def inicio_vista(request):
    listaC=Cliente.objects.all()
    return render(request,'gestionarCliente.html',{'listaClientes':listaC})

def registrarCliente(request):
    id_cliente=  request.POST['txtcliente']
    nombre=  request.POST['txtnombre']
    pago_total=  request.POST['txtpago_total']
    telefono=  request.POST['txttelefono']
    hora_compra=  request.POST['txthora_compra']
    cantidad_productos=  request.POST['txtcantidad_producto']
    dia_compra=  request.POST['txtdia_compra']
    guardarcliente=Cliente.objects.create(id_cliente=id_cliente,nombre=nombre,pago_total=pago_total,telefono=telefono,hora_compra=hora_compra,cantidad_productos=cantidad_productos,dia_compra=dia_compra)
    return redirect("/")

def seleccionarCliente(request,id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    return render(request,'editarCliente.html',{'c':cliente})

def editarCliente(request):
    id_cliente=  request.POST['txtcliente']
    nombre=  request.POST['txtnombre']
    pago_total=  request.POST['txtpago_total']
    telefono=  request.POST['txttelefono']
    hora_compra=  request.POST['txthora_compra']
    cantidad_productos=  request.POST['txtcantidad_producto']
    dia_compra=  request.POST['txtdia_compra']
    cliente= Cliente.objects.get(id_cliente=id_cliente)
    cliente.id_cliente =id_cliente
    cliente.nombre = nombre
    cliente.pago_total = pago_total
    cliente.telefono = telefono
    cliente.hora_compra = hora_compra
    cliente.cantidad_productos = cantidad_productos
    cliente.dia_compra = dia_compra
    cliente.save()
    return redirect("/")

def borrarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("/")
# Create your views here.

