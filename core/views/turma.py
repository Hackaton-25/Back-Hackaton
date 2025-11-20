from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models.turma import Course
from core.serializers.turma import CourseSerializer, CourseListSerializer


# -----------------------------
# Permissões locais
# -----------------------------
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.perfil in ["admin", "coordenador"]


# -----------------------------
# View principal
# -----------------------------
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all().order_by("-ano", "-semestre", "nome")

    def get_serializer_class(self):
        if self.action == "list":
            return CourseListSerializer
        return CourseSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdmin()]            # somente coord/admin gerenciam turmas
        return [IsAuthenticated()]        # alunos podem ver turmas

    # -----------------------------
    # Turmas do usuário logado
    # -----------------------------
    @action(detail=False, methods=["get"])
    def meus(self, request):
        user = request.user

        if user.perfil == "aluno":
            qs = user.turmas_inscrito.all()
        else:
            qs = user.turmas_que_coordena.all()

        return Response(CourseListSerializer(qs, many=True).data)

    # -----------------------------
    # Adicionar aluno
    # -----------------------------
    @action(detail=True, methods=["post"], permission_classes=[IsAdmin])
    def add_aluno(self, request, pk=None):
        curso = self.get_object()
        aluno_id = request.data.get("aluno_id")
        curso.alunos.add(aluno_id)
        return Response({"message": "Aluno adicionado com sucesso."})

    # -----------------------------
    # Remover aluno
    # -----------------------------
    @action(detail=True, methods=["post"], permission_classes=[IsAdmin])
    def remove_aluno(self, request, pk=None):
        curso = self.get_object()
        aluno_id = request.data.get("aluno_id")
        curso.alunos.remove(aluno_id)
        return Response({"message": "Aluno removido com sucesso."})
