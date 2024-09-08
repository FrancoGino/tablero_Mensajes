from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from .models import Mensajes

def base(request):
    # Crea una instancia del formulario ListarDestinatarios
    # Define un contexto que incluye el formulario y una URL
    context = {
    }
    # Renderiza la plantilla 'Mensajes/base.html' con el contexto proporcionado
    return render(request, 'Mensajes/base.html', context)