from django.shortcuts import render
import requests

# Create your views here.
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from .models import Nota
from .serializers import NotaSerializer
import requests

from django.conf import settings
import os
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        # Aquí puedes definir lo que quieres que suceda cuando se accede a esta ruta con GET
        return Response({"message": "Método GET no implementado"}, status=status.HTTP_501_NOT_IMPLEMENTED)




class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)



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
