from rest_framework import viewsets
from core.models.item_acervo import ItemAcervo
from core.serializers.item_acervo import ItemAcervoSerializer

class ItemAcervoViewSet(viewsets.ModelViewSet):
    queryset = ItemAcervo.objects.all().order_by('numero_acervo')
    serializer_class = ItemAcervoSerializer
