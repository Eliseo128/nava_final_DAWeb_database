from django.urls import path
from . import views
urlpatterns = [
    path('empleados',views.inicio_vistaEmpleados,name='empleados'),
    path('registrarEmpleados/',views.registrarEmpleados,  name='registrarEmpleados'),
    path('seleccionarEmpleado/<id_empleados>',views.seleccionarEmpleado,name="seleccionarEmpleado"),
    path('editarEmpleado/',views.editarEmpleado,name="editarEmpleado"),
    path("borrarEmpleado/<id_empleados>",views.borrarEmpleado,name="borrarEmpleado")
]