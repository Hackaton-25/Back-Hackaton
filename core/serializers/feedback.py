from rest_framework import serializers
from core.models.feedback import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.CharField(source="aluno.name", read_only=True)
    professor_nome = serializers.CharField(source="professor.name", read_only=True)
    turma_nome = serializers.CharField(source="turma.nome", read_only=True)

    class Meta:
        model = Feedback
        fields = [
            "id",
            "aluno",
            "aluno_nome",
            "professor",
            "professor_nome",
            "turma",
            "turma_nome",
            "texto",
            "nota_opcional",
            "criado_em",
        ]
        read_only_fields = ["criado_em"]
