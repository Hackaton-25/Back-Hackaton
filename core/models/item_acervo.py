from django.db import models

class ItemAcervo(models.Model):
    numero_acervo = models.CharField(max_length=100, unique=True)
    titulo = models.CharField(max_length=255)

    colecao = models.ForeignKey(
        'Colecao', on_delete=models.SET_NULL, null=True, blank=True
    )
    materia_prima = models.ForeignKey(
        'MateriaPrima', on_delete=models.SET_NULL, null=True, blank=True
    )
    subtipo_materia_prima = models.ForeignKey(
        'SubtipoMateriaPrima', on_delete=models.SET_NULL, null=True, blank=True
    )

    procedencia_origem = models.CharField(max_length=255, blank=True, null=True)
    datacao = models.CharField(max_length=255, blank=True, null=True)

    estado_conservacao = models.CharField(max_length=255, blank=True, null=True)

    localizacao_fisica = models.ForeignKey(
    'Localizacao',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='itens'
)


    descricao = models.TextField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.numero_acervo} - {self.titulo}"
