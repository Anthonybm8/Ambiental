from django.shortcuts import render, redirect
from .models import PaisajeSonoro
from .models import Empleado
from .models import Espacio
from django.contrib import messages

# Create your views here.
def paisajesonoro(request):
    return render(request, 'paisajesonoro.html')
def nuevoPaisajeSonoro(request):
    tartista = Empleado.objects.all()
    tespacio = Espacio.objects.all()
    return render(request, 'nuevoPaisajeSonoro.html', {'paisajesonoro': listadoPaisajesonoro})
def guardarPaisajeSonoro(request):
    titulo = request.POST["titulo"]
    fecha_creacion = request.POST["fecha_creacion"]
    duracion = request.POST["duracion"]
    descripcion = request.POST["descripcion"]
    artista = request.POST["artista"]
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
    return redirect('paisaje_sonoro')
