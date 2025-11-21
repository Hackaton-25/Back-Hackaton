from rest_framework import serializers
from core.models.coletor import Coletor

class ColetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coletor
        fields = '__all__'
        depth = 1