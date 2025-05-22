from django.urls import path
from . import views
urlpatterns = [
    path('espacio', views.espacio, name='espacio'),
    path('nuevoEspacio', views.espacio),
    path('guardarEspacio', views.guardarEspacio, name='guardarEspacio'),
]