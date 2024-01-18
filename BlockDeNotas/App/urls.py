from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotaViewSet

router = DefaultRouter()
router.register(r'notas', NotaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
