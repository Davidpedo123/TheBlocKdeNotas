from django.shortcuts import render
import requests

# Create your views here.
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from .models import Nota
from .serializers import NotaSerializer
from django.conf import settings
import os

#Esta clase es relacionada a lo que es la Api
class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    parser_classes = [MultiPartParser]
#Esta funcion permite la subida de audios y retorna un html donde se encuentra alojada los audios
def UploadAudios(request):
    audios = os.listdir(settings.MEDIA_ROOT)
    return render(request, 'audios.html', {'audios': audios})

#Esta funcion permite la llamada de la Api desde el html y retorna el html renderizado
def Notas(request):
    url = 'http://127.0.0.1:8000/notas/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()


    else:
        data = []

    return render(request, 'notas.html', {'data': data})
