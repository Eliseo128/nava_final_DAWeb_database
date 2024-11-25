from django.shortcuts import render,redirect
from .models import Sucursales

def inicio_vista(request):
    listaSur=Sucursales.objects.all()
    return render(request,'gestionarSurcursales.html',{'listaSurcursales':listaSur})

def registrarSurcursales(request):
    id_surcursal=  request.POST['txtsurcursal']
    ubicacion=  request.POST['txtubicacion']
    tamaño=  request.POST['txttamaño']
    capacidad=  request.POST['txtcapacidad']
    gerente=  request.POST['txtgerente']
    horario=  request.POST['txthorario']
    telefono=  request.POST['txttelefono']
    guardarsurcursal=Sucursales.objects.create(id_surcursal=id_surcursal,ubicacion=ubicacion,tamaño=tamaño,capacidad=capacidad,gerente=gerente,horario=horario,telefono=telefono)
    return redirect("/")

def seleccionarSurcursal(request,id_surcursal):
    surcursal = Sucursales.objects.get(id_surcursal=id_surcursal)
    return render(request,'editaSurcursal.html',{'c':surcursal})

def editarSurcursal(request):
    id_surcursal=  request.POST['txtsurcursal']
    ubicacion=  request.POST['txtubicacion']
    tamaño=  request.POST['txttamaño']
    capacidad=  request.POST['txtcapacidad']
    gerente=  request.POST['txtgerente']
    horario=  request.POST['txthorario']
    telefono=  request.POST['txttelefono']
    surcursal= Sucursales.objects.get(id_surcursal=id_surcursal)
    surcursal.id_surcursal =id_surcursal
    surcursal.ubicacion = ubicacion
    surcursal.tamaño = tamaño
    surcursal.capacidad=capacidad
    surcursal.gerente = gerente
    surcursal.horario = horario
    surcursal.telefono = telefono
    surcursal.save()
    return redirect("/")

def borrarSurcursal(request,id_surcursal):
    surcursal=Sucursales.objects.get(id_surcursal=id_surcursal)
    surcursal.delete()
    return redirect("/")
# Create your views here.


