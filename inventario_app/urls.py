from django.urls import path
from . import views
urlpatterns = [
    path('inventario',views.inicio_vistaInventario,name='inventario'),
    path('registrarInventario/',views.registrarInventario,  name='registrarInventario'),
    path('seleccionarInventario/<id_inventario>',views.seleccionarInventario,name="seleccionarInventario"),
    path('editarInventario/',views.editarInventario,name="editarInventario"),
    path("borrarInventario/<id_inventario>",views.borrarInventario,name="borrarProducto")
]