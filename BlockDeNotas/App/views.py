from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from .models import Nota
from .serializers import NotaSerializer
from django.conf import settings
import os


class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    parser_classes = [MultiPartParser]

def UploadAudios(request):
    audios = os.listdir(settings.MEDIA_ROOT)
    return render(request, 'audios.html', {'audios': audios})
