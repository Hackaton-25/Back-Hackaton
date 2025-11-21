from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from .models import (
    Auditoria,
    ItemAcervo,
    MovimentacaoItem,
    Colecao,
    Coletor,
    MateriaPrima,
    SubtipoMateriaPrima,
    Localizacao
)

# Lista de modelos monitorados
MONITORADAS = [
    ItemAcervo,
    MovimentacaoItem,
    Colecao,
    Coletor,
    MateriaPrima,
    SubtipoMateriaPrima,
    Localizacao
]


def registrar_auditoria(acao, instance, usuario=None):
    """
    Cria o registro de auditoria.
    - Se o modelo tiver um campo 'responsavel', ele será utilizado como usuário.
    - Caso contrário, ficará como None.
    """
    Auditoria.objects.create(
        usuario=getattr(instance, "responsavel", None) or usuario,
        acao=acao,
        modelo=instance.__class__.__name__,
        objeto_id=instance.id,
        descricao=str(instance)
    )


# ======================================================
# =============  SIGNAL ÚNICO PARA SAVE  ===============
# ======================================================

@receiver(post_save)
def auditoria_save(sender, instance, created, **kwargs):
    """
    Recebe save de todos os modelos.
    Filtra apenas os que estão em MONITORADAS.
    """
    if sender not in MONITORADAS:
        return

    acao = "CRIADO" if created else "ALTERADO"
    registrar_auditoria(acao, instance)


# ======================================================
# ============  SIGNAL ÚNICO PARA DELETE  ==============
# ======================================================

@receiver(post_delete)
def auditoria_delete(sender, instance, **kwargs):
    """
    Recebe delete de todos os modelos.
    Filtra apenas os que estão em MONITORADAS.
    """
    if sender not in MONITORADAS:
        return

    registrar_auditoria("DELETADO", instance)
