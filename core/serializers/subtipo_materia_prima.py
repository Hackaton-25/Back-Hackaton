from rest_framework import serializers
from core.models.subtipo_materia_prima import SubtipoMateriaPrima

class SubtipoMateriaPrimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubtipoMateriaPrima
        fields = '__all__'
