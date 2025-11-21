from rest_framework import viewsets
from core.models.imagem_item import ImagemItem
from core.serializers.imagem_item import ImagemItemSerializer

class ImagemItemViewSet(viewsets.ModelViewSet):
    queryset = ImagemItem.objects.all().order_by('-criado_em')
    serializer_class = ImagemItemSerializer
