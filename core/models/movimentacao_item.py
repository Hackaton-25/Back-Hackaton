from django.db import models

class MovimentacaoItem(models.Model):
    TIPO_MOVIMENTACAO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
        ('realocacao', 'Realocação'),
        ('retorno', 'Retorno'),
    ]

    item = models.ForeignKey(
        'ItemAcervo',
        on_delete=models.CASCADE,
        related_name='movimentacoes'
    )

    tipo = models.CharField(max_length=20, choices=TIPO_MOVIMENTACAO_CHOICES)

    localizacao_anterior = models.ForeignKey(
        'Localizacao',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='movimentacoes_anteriores'
    )

    localizacao_nova = models.ForeignKey(
        'Localizacao',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='movimentacoes_novas'
    )

    motivo = models.CharField(max_length=255, blank=True, null=True)

    data_movimentacao = models.DateTimeField(auto_now_add=True)

    responsavel = models.ForeignKey(
        'core.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.item.numero_acervo} - {self.tipo} ({self.data_movimentacao.date()})"
