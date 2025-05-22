from django.urls import path
from . import views
urlpatterns = [
    path('espacio', views.espacio, name='espacio'),
    path('nuevoEspacio', views.nuevoEspacio , name='nuevoEspacio'),
    path('guardarEspacio', views.guardarEspacio, name='guardarEspacio'),
    path('editarEspacio/<int:id>', views.editarEspacio, name='editarEspacio'),
    path('actualizarEspacio/<int:id>', views.actualizarEspacio, name='actualizarEspacio'),
    path('eliminarEspacio/<int:id>', views.eliminarEspacio, name='eliminarEspacio'),
]