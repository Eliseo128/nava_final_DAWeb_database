from django.urls import path
from . import views
urlpatterns = [
    path('',views.inicio_vista,name='gestionarSurcursales.html'),
    path('registrarSurcursales/',views.registrarSurcursales, name='registrarSurcursales'),
    path('seleccionarSurcursal/<id_surcursal>',views.seleccionarSurcursal,name="seleccionarSurcursal"),
    path('editarSurcursal/',views.editarSurcursal,name="editarSurcursal"),
    path("borrarSurcursal/<id_surcursal>",views.borrarSurcursal,name="borrarSurcursal")
]