from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django import forms
from .models import Mensajes
from django_tables2 import SingleTableView
from .tabla import MensajesTabla


def base(request):
    return render(request, 'home.html')


class ShowMensajesRecibidos(View):
    def get(self,request):
        form = ListarMensajes(seleccion = 'destinatario')
        context = {
            'form': form,
            'url': 'http://localhost:8000/mensajes_recibidos/',
        }
        return render(request, 'mensajes/show_mensajes.html', context)
    def post(self,request):
            form = ListarMensajes(seleccion = 'destinatario')
            seleccion = request.POST.get('form')
            mensajes = Mensajes.objects.filter(destinatario=seleccion)
            tabla = MensajesTabla(mensajes)
            context = {
                'form': form,
                'mensajes': tabla,
                'seleccion': seleccion,
            }
            return render(request, 'mensajes/show_mensajes.html', context)

class ShowMensajesEnviados(View):
    def get(self,request):
        form = ListarMensajes(seleccion = 'remitente')
        context = {
            'form': form,
            'url': 'http://localhost:8000/mensajes_enviados/',
        }
        return render(request, 'mensajes/show_mensajes.html', context)
    def post(self,request):
            form = ListarMensajes(seleccion = 'remitente')
            seleccion = request.POST.get('form')
            mensajes = Mensajes.objects.filter(destinatario=seleccion)
            tabla = MensajesTabla(mensajes)
            context = {
                'form': form,
                'mensajes': tabla,
                'seleccion': seleccion,
            }
            return render(request, 'mensajes/show_mensajes.html', context)



class CrearMensaje(View):
    def get(self,request):
        form = MensajesForm()

        return render(request, 'mensajes/new_mensajes.html', {'form': form, 'url': request.path})
    def post(self,request):
        form = MensajesForm(request.POST)
        if form.is_valid():
            Mensajes.objects.create(
                remitente=form.cleaned_data['remitente'],
                destinatario=form.cleaned_data['destinatario'],
                texto=form.cleaned_data['texto']
            )
            return redirect('/') 
        
class EliminarMensaje(View):
        def get(self, request, id):
            print("eliminar mensaje")
            mensaje = get_object_or_404(Mensajes, id=id)
            mensaje.delete()
            return redirect('/')


class ListarMensajes(forms.Form):
    def __init__(self, *args, seleccion=None, **kwargs):
        super(ListarMensajes, self).__init__(*args, **kwargs)
        if hasattr(Mensajes, seleccion):
            nombres = [(mensaje, mensaje) for mensaje in Mensajes.objects.values_list(seleccion, flat=True).distinct()]
        self.fields['form'].choices = nombres
    form = forms.ChoiceField(
        choices=[],
        widget=forms.Select,
    )

class MensajesListView(SingleTableView):
    model = Mensajes
    table_class = MensajesTabla
    template_name = 'mensajes/tabla.html'

class MensajesForm(forms.Form):
    remitente = forms.CharField(label='Remitente', max_length=100)
    destinatario = forms.CharField(label='Destinatario', max_length=100)
    texto = forms.CharField(label='Texto', widget=forms.Textarea)