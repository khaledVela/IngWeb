from django.urls import path, include
from rest_framework import routers

from .views import InvitadosCasaViewSet, InvitadosAreaComunViewSet

router = routers.DefaultRouter()
router.register(r'invitadoscasa', InvitadosCasaViewSet)
router.register(r'invitadosareacomun', InvitadosAreaComunViewSet)

urlpatterns = [
    path('', include(router.urls))
]