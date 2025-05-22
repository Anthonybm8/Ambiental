from django.shortcuts import render, redirect
from .models import Espacio
from django.contrib import messages

# Create your views here.
def espacio(request):
    lista_espacios = Espacio.objects.all()
    return render(request, 'espacio.html', {'lista_espacios': lista_espacios})

def nuevoEspacio(request):
    return render(request, 'nuevoEspacio.html')

def guardarEspacio(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        ubicacion = request.POST.get('ubicacion')
        descripcion = request.POST.get('descripcion')

        if nombre and tipo and ubicacion:
            Espacio.objects.create(
                nombre=nombre,
                tipo=tipo,
                ubicacion=ubicacion,
                descripcion=descripcion
            )
            messages.success(request, 'Espacio guardado correctamente.')
            return redirect('espacio')
        else:
            messages.error(request, 'Todos los campos son obligatorios.')
            return redirect('nuevoEspacio')
    else:
        return redirect('espacio')