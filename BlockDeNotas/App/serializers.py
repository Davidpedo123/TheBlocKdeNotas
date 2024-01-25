from rest_framework import serializers
from .models import Nota
#Este archivo serializa el modelo y lo convierte a formato json
class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ['id', 'titulo', 'contenido', 'audio','fecha_creacion', 'fecha_modificacion']
