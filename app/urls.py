from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views.user import UserViewSet
from core.views.turma import CourseViewSet
from core.views.matricula import EnrollmentViewSet
from core.views.atividade import ActivityViewSet
from core.views.entrega import SubmissionViewSet
from core.views.feedback import FeedbackViewSet

router = DefaultRouter()
router.register(r"usuarios", UserViewSet, basename="usuarios")
router.register(r"turmas", CourseViewSet, basename="turmas")
router.register(r"matriculas", EnrollmentViewSet, basename="matriculas")
router.register(r"atividades", ActivityViewSet, basename="atividades")
router.register(r"entregas", SubmissionViewSet, basename="entregas")
router.register(r"feedbacks", FeedbackViewSet, basename="feedbacks")

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
]
