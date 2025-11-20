from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models.user import User
from core.serializers.user import (
    UserSerializer,
    UserListSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
)


# -----------------------------
# Permissões locais
# -----------------------------
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.perfil in ["admin", "coordenador"]


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.perfil in ["admin", "coordenador"]:
            return True
        return obj.id == request.user.id


# -----------------------------
# View principal
# -----------------------------
class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("id")
    search_fields = ["name", "email", "turma", "escola"]
    filterset_fields = ["perfil", "turma", "escola"]

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        if self.action in ["update", "partial_update"]:
            return UserUpdateSerializer
        if self.action == "list":
            return UserListSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]                     # cadastro aberto
        if self.action == "list":
            return [IsAdmin()]                     # coord/admin veem todos
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrAdmin()]
        return [IsAuthenticated()]

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        return Response(UserSerializer(request.user).data)
