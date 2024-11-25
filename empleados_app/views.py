from django.shortcuts import render,redirect
from .models import Empleados

def inicio_vistaEmpleados(request):
    listaE=Empleados.objects.all()
    return render(request,'gestionarEmpleados.html',{'listaEmpleados':listaE})

def registrarEmpleados(request):
    id_empleados=  request.POST['txtempleado']
    nombre=  request.POST['txtnombre']
    edad=  request.POST['txtedad']
    curp=  request.POST['txtcurp']
    telefono=  request.POST['txtelefono']
    horario=  request.POST['txthorario']
    paga=  request.POST['txtpaga']
    guardarempleado=Empleados.objects.create(id_empleados=id_empleados,nombre=nombre,edad=edad,curp=curp,telefono=telefono,horario=horario,paga=paga)
    return redirect("empleados")

def seleccionarEmpleado(request,id_empleados):
    empleado = Empleados.objects.get(id_empleados=id_empleados)
    return render(request,'editarEmpleado.html',{'p':empleado})

def editarEmpleado(request):
    id_empleados=  request.POST['txtempleado']
    nombre=  request.POST['txtnombre']
    edad=  request.POST['txtedad']
    curp=  request.POST['txtcurp']
    telefono=  request.POST['txtelefono']
    horario=  request.POST['txthorario']
    paga=  request.POST['txtpaga']
    empleado= Empleados.objects.get(id_empleados=id_empleados)
    empleado.id_empleados =id_empleados
    empleado.nombre = nombre
    empleado.edad = edad
    empleado.curp = curp
    empleado.telefono = telefono
    empleado.horario = horario
    empleado.paga = paga
    empleado.save()
    return redirect("empleados")

def borrarEmpleado(request,id_empleados):
    empleado=Empleados.objects.get(id_empleados=id_empleados)
    empleado.delete()
    return redirect("empleados")
# Create your views here.
