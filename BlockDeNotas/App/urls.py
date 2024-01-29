from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotaViewSet, UploadAudios, Notas, register
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf.urls.static import static

#Aqui se encuentra las url
router = DefaultRouter()
router.register(r'notas', NotaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('audios/', UploadAudios, name='audios'),
    path('notas/prueba', Notas, name='notas'),
    path('register/', register, name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
