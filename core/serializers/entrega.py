from rest_framework import serializers
from core.models.entrega import Submission

class SubmissionSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.CharField(source="aluno.name", read_only=True)
    atividade_titulo = serializers.CharField(source="atividade.titulo", read_only=True)

    class Meta:
        model = Submission
        fields = [
            "id",
            "atividade",
            "atividade_titulo",
            "aluno",
            "aluno_nome",
            "texto_resposta",
            "arquivo",
            "nota",
            "data_envio",
        ]
        read_only_fields = ["data_envio"]
