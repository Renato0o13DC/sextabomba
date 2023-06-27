
from django.urls import path
from .views import index, especialidades, ubicacion, contacto, mostrarCarros, agregarCarro,modificarCarro, elminar_carro


urlpatterns = [
    path('', index, name="index"),
    path('especialidades/', especialidades, name="especialidades"),
    path('ubicacion/', ubicacion, name="ubicacion"),
    path('contacto/', contacto, name="contacto"),
    path('mostrarCarros/', mostrarCarros, name="Mostrar Carros"),
    path('agregar-carro/', agregarCarro, name="Agregar_Carro"),
    path('modificar-carro/<patente>/', modificarCarro, name="Modificar_Carro"),
    path('eliminar-carro/<patente>/ ', elminar_carro, name="Eliminar_Carro"),
]   
