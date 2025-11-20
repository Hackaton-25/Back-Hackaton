from rest_framework import viewsets, filters
from core.models.matricula import Enrollment
from core.serializers.matricula import EnrollmentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["aluno__nome", "turma__nome", "status"]
