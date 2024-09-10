import django_tables2 as tables
from django.urls import reverse
from .models import Mensajes

class MensajesTabla(tables.Table):
    accion = tables.TemplateColumn(
            template_name="includes/accion.html",
            orderable=False
        )
    class Meta:
        model = Mensajes
        template_name = "django_tables2/bootstrap.html"
        fields = ("remitente", "texto", "fecha_hora", 'accion')