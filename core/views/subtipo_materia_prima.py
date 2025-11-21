from rest_framework import viewsets
from core.models.subtipo_materia_prima import SubtipoMateriaPrima
from core.serializers.subtipo_materia_prima import SubtipoMateriaPrimaSerializer

class SubtipoMateriaPrimaViewSet(viewsets.ModelViewSet):
    queryset = SubtipoMateriaPrima.objects.all().order_by('nome')
    serializer_class = SubtipoMateriaPrimaSerializer
