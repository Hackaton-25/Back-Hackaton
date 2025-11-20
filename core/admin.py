"""
Django admin customization para o sistema escolar.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models.user import User
from core.models.turma import Course
from core.models.matricula import Enrollment
from core.models.atividade import Activity
from core.models.entrega import Submission
from core.models.feedback import Feedback


# ------------------------
# User Admin
# ------------------------

class UserAdmin(BaseUserAdmin):
    """Configuração do admin para usuários."""
    ordering = ["id"]
    list_display = ["email", "name", "perfil"]
    readonly_fields = ["last_login"]

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Informações pessoais"), {"fields": ("name", "perfil")}),
        (
            _("Permissões"),
            {"fields": ("is_active", "is_staff", "is_superuser")},
        ),
        (_("Datas importantes"), {"fields": ("last_login",)}),
        (_("Grupos"), {"fields": ("groups",)}),
        (_("Permissões de usuário"), {"fields": ("user_permissions",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "perfil",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )

admin.site.register(User, UserAdmin)


# ------------------------
# Course / Turma
# ------------------------
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("nome", "professor_responsavel")
    search_fields = ("nome", "professor_responsavel__name")
    list_filter = ("professor_responsavel",)


# ------------------------
# Enrollment
# ------------------------
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("aluno", "turma", "status")
    search_fields = ("aluno__name", "turma__nome")
    list_filter = ("status", "turma")


# ------------------------
# Activity
# ------------------------
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("titulo", "turma", "data_criacao", "data_entrega")
    search_fields = ("titulo", "turma__nome")
    list_filter = ("turma", "data_entrega")


# ------------------------
# Submission
# ------------------------
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "atividade", "data_envio")
    list_filter = ("atividade", "data_envio")
    search_fields = ("atividade__titulo", "aluno__name")



# ------------------------
# Feedback
# ------------------------
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("aluno", "professor", "turma", "nota_opcional", "criado_em")
    search_fields = ("aluno__name", "professor__name", "turma__nome")
    list_filter = ("turma", "professor", "nota_opcional")
