# urls.py
from django.urls import path
from django.views import View
from . import views
from .views import ShowMensajesRecibidos, ShowMensajesEnviados, CrearMensaje, EliminarMensaje

urlpatterns = [
    path('', views.base, name='base'),
    path('crear_mensaje/', CrearMensaje.as_view(), name='crear_mensaje'),
    path('mensajes_recibidos/', ShowMensajesRecibidos.as_view(), name='mensajes_recibidos'),
    path('mensajes_enviados/', ShowMensajesEnviados.as_view(), name='mensajes_enviados'),
    path('eliminar_mensaje/<int:id>', EliminarMensaje.as_view(), name='eliminar_mensaje'),
]