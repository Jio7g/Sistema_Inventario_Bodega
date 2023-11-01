from django.urls import path
from . import views

urlpatterns = [
    path('ingresar_producto/', views.ingresar_producto, name='ingresar_producto'),
    path('registrar_salida/', views.registrar_salida, name='registrar_salida'),
    path('consultar_inventario/', views.consultar_inventario, name='consultar_inventario'),
]
