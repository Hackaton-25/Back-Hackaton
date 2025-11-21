from rest_framework import viewsets
from core.models.coletor import Coletor
from core.serializers.coletor import ColetorSerializer

class ColetorViewSet(viewsets.ModelViewSet):
    queryset = Coletor.objects.all().order_by('nome')
    serializer_class = ColetorSerializer
