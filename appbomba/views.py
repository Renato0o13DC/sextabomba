from django.shortcuts import render, redirect, get_object_or_404
from .models import CarroBomba
from .forms import CarroForm
# Create your views here.

def index (request):
    return render(request, 'appbomba/index.html')

def contacto (request):
    return render(request, 'appbomba/contacto.html')

def ubicacion (request):
    return render(request, 'appbomba/ubicacion.html')

def especialidades (request):
    return render(request, 'appbomba/especialidades.html')


def mostrarCarros (request):
    carros = CarroBomba.objects.all()
    return render(request, 'appbomba/mostrarCarros.html', {"carros":carros})

def agregarCarro(request):
    
    data={
        'form': CarroForm()
    }

    
    if request.method =='POST':
        formulario = CarroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario

    return render(request, 'appbomba/carros/agregar.html', data)


def modificarCarro(request, patente):

    Carro= get_object_or_404(CarroBomba, patente=patente)

    data={
        'form': CarroForm(instance=Carro)
    }

    if request.method == 'POST':
        formulario = CarroForm(data=request.POST, instance=Carro)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="Mostrar Carros")
        data["form"] = formulario


    return render(request, 'appbomba/carros/modificar.html', data)

def elminar_carro(request, patente):
    Carro= get_object_or_404(CarroBomba, patente=patente)
    Carro.delete()
    return redirect(to="Mostrar Carros")