from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotaViewSet, UploadAudios, Notas
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static

#Aqui se encuentra las url
router = DefaultRouter()
router.register(r'notas', NotaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('audios/', UploadAudios, name='audios'),
    path('notas/prueba', Notas, name='notas'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
