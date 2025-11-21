from rest_framework import serializers
from core.models.imagem_item import ImagemItem

class ImagemItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagemItem
        fields = '__all__'
