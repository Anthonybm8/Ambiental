from django.shortcuts import render, redirect
from .models import Empleado
from django.contrib import messages

def empleado(request):
    lista_empleados = Empleado.objects.all()
    return render(request, 'empleado.html', {'lista_empleados': lista_empleados})

def nuevoEmpleado(request):
    return render(request, 'nuevoEmpleado.html')

def guardarEmpleado(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        tipo_empleado = request.POST.get('tipo_empleado')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')

        if nombre and apellido and tipo_empleado and email and telefono:
            Empleado.objects.create(
                nombre=nombre,
                apellido=apellido,
                tipo_empleado=tipo_empleado,
                email=email,
                telefono=telefono
            )
            messages.success(request, 'Empleado guardado correctamente.')
            return redirect('empleado')
        else:
            messages.error(request, 'Todos los campos son obligatorios.')
            return redirect('nuevoEmpleado')
    else:
        return redirect('empleado')

def editarEmpleado(request, id):
    empleado = Empleado.objects.get(id=id)
    return render(request, 'editarEmpleado.html', {'empleado': empleado})     

def actualizarEmpleado(request, id):
    if request.method == 'POST':
        empleado = Empleado.objects.get(id=id)
        empleado.nombre = request.POST.get('nombre')
        empleado.apellido = request.POST.get('apellido')
        empleado.tipo_empleado = request.POST.get('tipo_empleado')
        empleado.email = request.POST.get('email')
        empleado.telefono = request.POST.get('telefono')
        empleado.save()
        messages.success(request, 'Empleado actualizado correctamente.')
        return redirect('empleado')
    else:
        return redirect('empleado')  