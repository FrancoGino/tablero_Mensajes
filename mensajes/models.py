from django.db import models

class Mensajes (models.Model):
    remitente = models.CharField(max_length=15)
    destinatario = models.CharField(max_length=15)
    texto = models.TextField()
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.remitente