from rest_framework import viewsets, serializers
# Create your views here.

from .models import InvitadosCasa, InvitadosAreaComun

class InvitadosCasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitadosCasa
        fields = '__all__'

class InvitadosCasaViewSet(viewsets.ModelViewSet):
    queryset = InvitadosCasa.objects.all()
    serializer_class = InvitadosCasaSerializer

class InvitadosAreaComunSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitadosAreaComun
        fields = '__all__'

class InvitadosAreaComunViewSet(viewsets.ModelViewSet):
    queryset = InvitadosAreaComun.objects.all()
    serializer_class = InvitadosAreaComunSerializer