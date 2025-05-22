from django.urls import path
from . import views

urlpatterns = [
    path('paisajesonoro', views.paisajesonoro, name='sonoro'),
    path('nuevoPaisajeSonoro', views.nuevoPaisajeSonoro, name='nuevoPaisaje'),
    path('guardarPaisajeSonoro', views.guardarPaisajeSonoro, name='guardarPaisajeSonoro'),
    path('editarPaisajeSonoro/<int:id>', views.editarPaisajeSonoro, name='editarPaisajeSonoro'),
    #path('actualizarPaisajeSonoro/<int:id>', views.actualizarPaisajeSonoro, name='actualizarPaisajeSonoro'),
    #path('eliminarPaisajeSonoro/<int:id>', views.eliminarPaisajeSonoro, name='eliminarPaisajeSonoro'),
]