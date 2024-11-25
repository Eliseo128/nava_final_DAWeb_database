from django.urls import path
from . import views
urlpatterns = [
    path('',views.inicio_vista,name='gestionarProductos.html'),
    path('registrarProducto/',views.registrarProducto,  name='registrarProducto'),
    path('seleccionarProducto/<id_producto>',views.seleccionarProducto,name="seleccionarProducto"),
    path('editarProducto/',views.editarProducto,name="editarProducto"),
    path("borrarProducto/<id_producto>",views.borrarProducto,name="borrarProducto")
]