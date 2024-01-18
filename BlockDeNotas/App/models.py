

from django.db import models


class Nota(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    audio = models.FileField(upload_to='')

    def __str__(self):
        return self.titulo
