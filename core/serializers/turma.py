from rest_framework import serializers
from core.models.turma import Course
from core.serializers.user import UserListSerializer
from core.models.user import User


class CourseListSerializer(serializers.ModelSerializer):
    professor_responsavel = UserListSerializer()

    class Meta:
        model = Course
        fields = ["id", "nome", "ano", "semestre", "professor_responsavel"]

class CourseSerializer(serializers.ModelSerializer):
    alunos = UserListSerializer(many=True, read_only=True)
    professor_responsavel = UserListSerializer(read_only=True)
    professor_responsavel_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(perfil="professor"),
        write_only=True,
        source="professor_responsavel"
    )

    class Meta:
        model = Course
        fields = [
            "id", "nome", "descricao",
            "ano", "semestre",
            "professor_responsavel", "professor_responsavel_id",
            "alunos",
        ]


