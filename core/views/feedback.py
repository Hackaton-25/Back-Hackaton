from rest_framework import viewsets, permissions, filters
from core.models.feedback import Feedback
from core.serializers.feedback import FeedbackSerializer

class IsProfessorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.perfil == "professor"

class IsOwnerOrAdminReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # aluno só vê feedback próprio
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_staff or obj.aluno == request.user
        # professor ou admin edita
        return request.user.is_staff or obj.professor == request.user

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["texto", "aluno__name", "professor__name"]
    ordering_fields = ["criado_em"]

    def get_permissions(self):
        if self.action in ["create"]:
            return [IsProfessorOrAdmin()]
        return [IsOwnerOrAdminReadOnly()]
