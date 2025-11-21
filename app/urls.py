from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views.user import UserViewSet
from core.views.item_acervo import ItemAcervoViewSet
from core.views.colecao import ColecaoViewSet
from core.views.coletor import ColetorViewSet
from core.views.materia_prima import MateriaPrimaViewSet
from core.views.subtipo_materia_prima import SubtipoMateriaPrimaViewSet
from core.views.imagem_item import ImagemItemViewSet
from core.views.movimentacao_item import MovimentacaoItemViewSet
from core.views.auditoria import AuditoriaViewSet
from core.views.localizacao import LocalizacaoViewSet
from core.views.login import login_view

router = DefaultRouter()
router.register(r"usuarios", UserViewSet, basename="usuarios")
router.register(r"itens-acervo", ItemAcervoViewSet, basename="itens-acervo")
router.register(r"colecoes", ColecaoViewSet, basename="colecoes")
router.register(r"coletores", ColetorViewSet, basename="coletores")
router.register(r"materias-primas", MateriaPrimaViewSet, basename="materias-primas")
router.register(r"subtipos-materias-primas", SubtipoMateriaPrimaViewSet, basename="subtipos-materias-primas")
router.register(r"imagens-itens", ImagemItemViewSet, basename="imagens-itens")
router.register(r"movimentacoes-itens", MovimentacaoItemViewSet, basename="movimentacoes-itens")
router.register(r"auditorias", AuditoriaViewSet, basename="auditorias")
router.register(r"localizacoes", LocalizacaoViewSet, basename="localizacoes")
urlpatterns = [
    path("admin/", admin.site.urls),

    # OpenAPI 3 schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    # Swagger UI
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),

    # Redoc UI
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    # API endpoints
    path("api/", include(router.urls)),
    path("api/login-hack/", login_view, name="login"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
