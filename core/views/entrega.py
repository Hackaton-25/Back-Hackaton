from rest_framework import viewsets, permissions, filters
from core.models.entrega import Submission
from core.serializers.entrega import SubmissionSerializer

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.aluno == request.user

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["aluno__name", "atividade__titulo"]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdmin()]
        return [permissions.IsAuthenticated()]
