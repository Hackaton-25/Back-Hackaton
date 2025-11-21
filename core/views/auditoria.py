from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from core.models.auditoria import Auditoria
from core.serializers.auditoria import AuditoriaSerializer

class AuditoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Auditoria.objects.all().order_by('-data')
    serializer_class = AuditoriaSerializer
    permission_classes = [IsAdminUser]
