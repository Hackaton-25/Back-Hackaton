from rest_framework import viewsets
from core.models.movimentacao_item import MovimentacaoItem
from core.serializers.movimentacao_item import MovimentacaoItemSerializer

class MovimentacaoItemViewSet(viewsets.ModelViewSet):
    queryset = MovimentacaoItem.objects.all().order_by('-data_movimentacao')
    serializer_class = MovimentacaoItemSerializer
