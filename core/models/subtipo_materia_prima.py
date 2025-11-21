from django.db import models

class SubtipoMateriaPrima(models.Model):
    nome = models.CharField(max_length=100)

    materia_prima = models.ForeignKey(
        'MateriaPrima', 
        on_delete=models.CASCADE,
        related_name='subtipos'
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('nome', 'materia_prima')

    def __str__(self):
        return f"{self.nome} ({self.materia_prima.nome})"
