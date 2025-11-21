from rest_framework import viewsets
from core.models.materia_prima import MateriaPrima
from core.serializers.materia_prima import MateriaPrimaSerializer

class MateriaPrimaViewSet(viewsets.ModelViewSet):
    queryset = MateriaPrima.objects.all().order_by('nome')
    serializer_class = MateriaPrimaSerializer
