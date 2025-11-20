from rest_framework import serializers
from core.models.matricula import Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.CharField(source="aluno.nome", read_only=True)
    turma_nome = serializers.CharField(source="turma.nome", read_only=True)

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "aluno",
            "aluno_nome",
            "turma",
            "turma_nome",
            "status",
            "created_at"
        ]
        read_only_fields = ["created_at"]
