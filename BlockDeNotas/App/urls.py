from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotaViewSet, UploadAudios
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'notas', NotaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('audios/', UploadAudios, name='audios')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
