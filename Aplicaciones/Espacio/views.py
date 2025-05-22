from django.shortcuts import render, redirect
from .models import Espacio
from django.contrib import messages

# Create your views here.
def espacio(request):
    lista_espacios = Espacio.objects.all()
    return render(request, 'espacio.html', {'lista_espacios': lista_espacios})