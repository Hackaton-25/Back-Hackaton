from rest_framework import serializers
from core.models.item_acervo import ItemAcervo

class ItemAcervoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemAcervo
        fields = '__all__'
        depth = 1