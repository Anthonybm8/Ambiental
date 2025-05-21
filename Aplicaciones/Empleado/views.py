from django.shortcuts import render,redirect
from .models import Empleado
from django.contrib import messages

def empleado(request):
    lista_empleados = Empleado.objects.all()
    return render(request, 'empleado.html', {'lista_empleados': lista_empleados})

# Create your views here.
