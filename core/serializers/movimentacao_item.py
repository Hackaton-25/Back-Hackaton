from rest_framework import serializers
from core.models.movimentacao_item import MovimentacaoItem

class MovimentacaoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimentacaoItem
        fields = '__all__'
        depth = 1
