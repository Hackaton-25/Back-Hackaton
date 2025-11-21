from django.db import models

class Auditoria(models.Model):
    ACAO_CHOICES = [
        ('create', 'Criação'),
        ('update', 'Atualização'),
        ('delete', 'Exclusão'),
    ]

    usuario = models.ForeignKey(
        'core.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    acao = models.CharField(max_length=20, choices=ACAO_CHOICES)

    # Modelo afetado (nome do model)
    modelo = models.CharField(max_length=255)

    # ID do registro afetado
    objeto_id = models.IntegerField(null=True, blank=True)

    # Resumo da mudança
    descricao = models.TextField(blank=True, null=True)

    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.modelo} ({self.acao}) por {self.usuario}"
