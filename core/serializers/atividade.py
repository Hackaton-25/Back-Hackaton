from rest_framework import serializers
from core.models.atividade import Activity

class ActivitySerializer(serializers.ModelSerializer):
    turma_nome = serializers.CharField(source="turma.nome", read_only=True)

    class Meta:
        model = Activity
        fields = [
            "id",
            "turma",
            "turma_nome",
            "titulo",
            "descricao",
            "data_criacao",
            "data_entrega",
        ]
        read_only_fields = ["data_criacao"]
