"""
Django admin customization para o sistema escolar.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models.user import User
from core.models.item_acervo import ItemAcervo
from core.models.colecao import Colecao
from core.models.coletor import Coletor
from core.models.materia_prima import MateriaPrima
from core.models.subtipo_materia_prima import SubtipoMateriaPrima
from core.models.imagem_item import ImagemItem
from core.models.movimentacao_item import MovimentacaoItem
from core.models.auditoria import Auditoria
from core.models.localizacao import Localizacao


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
# Item Acervo
# ------------------------

@admin.register(ItemAcervo)
class ItemAcervoAdmin(admin.ModelAdmin):
    list_display = ('numero_acervo', 'titulo',)
    search_fields = ('numero_acervo', 'titulo',)
    list_filter = ('colecao', 'materia_prima', 'localizacao_fisica')


# ------------------------
# Coleção
# ------------------------

@admin.register(Colecao)
class ColecaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)


# ------------------------
# Coletor
# ------------------------

@admin.register(Coletor)
class ColetorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


# ------------------------
# Matéria Prima
# ------------------------

@admin.register(MateriaPrima)
class MateriaPrimaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


# ------------------------
# Subtipo Matéria Prima
# ------------------------

@admin.register(SubtipoMateriaPrima)
class SubtipoMateriaPrimaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


# ------------------------
# Imagem Item
# ------------------------

@admin.register(ImagemItem)
class ImagemItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'imagem', 'criado_em')
    search_fields = ('item__numero_acervo', 'item__titulo')


# ------------------------
# Movimentação Item
# ------------------------

@admin.register(MovimentacaoItem)
class MovimentacaoItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'data_movimentacao', 'tipo', 'responsavel')
    search_fields = ('item__numero_acervo', 'item__titulo', 'responsavel__email')
    list_filter = ('tipo', 'localizacao_anterior', 'localizacao_nova')


# ------------------------
# Auditoria
# ------------------------

@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'acao', 'data')
    search_fields = ('usuario__email', 'acao')


# ------------------------
# Localização
# ------------------------

@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'tipo')
    search_fields = ('nome',)
