from django.urls import path
from . import views
urlpatterns = [
    path('empleado', views.empleado, name='empleado'),
    path('nuevoEmpleado', views.nuevoEmpleado),
    path('guardarEmpleado', views.guardarEmpleado, name='guardarEmpleado'),
]