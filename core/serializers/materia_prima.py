from rest_framework import serializers
from core.models.materia_prima import MateriaPrima

class MateriaPrimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MateriaPrima
        fields = '__all__'
        depth = 1
