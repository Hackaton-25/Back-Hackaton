from rest_framework import viewsets, filters
from core.models.atividade import Activity
from core.serializers.atividade import ActivitySerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["titulo", "descricao", "turma__nome"]
