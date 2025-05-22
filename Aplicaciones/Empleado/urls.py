from django.urls import path
from . import views
urlpatterns = [
    path('empleado', views.empleado, name='empleado'),
    path('nuevoEmpleado', views.nuevoEmpleado),
    path('guardarEmpleado', views.guardarEmpleado, name='guardarEmpleado'),
    path('editarEmpleado/<int:id>', views.editarEmpleado, name='editarEmpleado'),
    path('actualizarEmpleado/<int:id>', views.actualizarEmpleado, name='actualizarEmpleado'),
    path('eliminarEmpleado/<int:id>', views.eliminarEmpleado, name='eliminarEmpleado'),
]