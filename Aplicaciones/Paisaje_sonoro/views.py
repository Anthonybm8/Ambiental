from django.shortcuts import render, redirect
from .models import PaisajeSonoro
from .models import Empleado
from .models import Espacio
from django.contrib import messages

# Create your views here.
def paisajesonoro(request):
    listadoPaisajesonoro = PaisajeSonoro.objects.all()
    return render(request, 'paisaje_sonoro.html', {'paisajesonoro': listadoPaisajesonoro})

def nuevoPaisajeSonoro(request):
    tartista = Empleado.objects.all()
    tespacio = Espacio.objects.all()
    return render(request, 'nuevoPaisaje.html', {'empleados': tartista, 'espacios': tespacio})

def guardarPaisajeSonoro(request):
    titulo = request.POST["titulo"]
    fecha_creacion = request.POST["fecha_creacion"]
    duracion = request.POST["duracion"]
    descripcion = request.POST["descripcion"]
    artista = request.POST["empleado"]
    artista = Empleado.objects.get(id=artista)
    espacio = request.POST["espacio"]
    espacio = Espacio.objects.get(id=espacio)
    nuevoPaisajeSonoro = PaisajeSonoro.objects.create(
        titulo=titulo,
        fecha_creacion=fecha_creacion,
        duracion=duracion,
        descripcion=descripcion,
        artista=artista,
        espacio=espacio
    )
    messages.success(request,"paisaje guardado exitosamente")
    return redirect('sonoro')

def editarPaisajeSonoro(request, id):
    paisajesonoroeditar = PaisajeSonoro.objects.get(id=id)
    tartista = Empleado.objects.all()
    tespacio = Espacio.objects.all()
    return render(request, 'editarPaisajeSonoro.html', {'p': paisajesonoroeditar, 'empleados': tartista, 'espacios': tespacio})

def procesoEdicionPaisajeSonoro(request):
    id = request.POST["id"]
    paisajesonoroeditar = PaisajeSonoro.objects.get(id=id)
    paisajesonoroeditar.titulo = request.POST["titulo"]
    paisajesonoroeditar.fecha_creacion = request.POST["fecha_creacion"]
    paisajesonoroeditar.duracion = request.POST["duracion"]
    paisajesonoroeditar.descripcion = request.POST["descripcion"]
    paisajesonoroeditar.artista = request.POST["artista"]
    paisajesonoroeditar.espacio = request.POST["espacio"]
    paisajesonoroeditar = Empleado.objects.get(id=paisajesonoroeditar.artista)
    paisajesonoroeditar=Espacio.objects.get(id=paisajesonoroeditar.espacio)
    paisajesonoro=PaisajeSonoro.objects.get(id=id)

    paisajesonoroeditar.save()
    messages.success(request,"paisaje editado exitosamente")
    return redirect('paisaje_sonoro')