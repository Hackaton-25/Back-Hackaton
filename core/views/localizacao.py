from rest_framework import viewsets
from core.models.localizacao import Localizacao
from core.serializers.localizacao import LocalizacaoSerializer

class LocalizacaoViewSet(viewsets.ModelViewSet):
    queryset = Localizacao.objects.all().order_by('nome')
    serializer_class = LocalizacaoSerializer
