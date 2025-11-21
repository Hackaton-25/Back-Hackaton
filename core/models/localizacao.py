from django.db import models

class Localizacao(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=True, null=True)

    tipo = models.CharField(
        max_length=50,
        choices=[
            ('reserva', 'Reserva Técnica'),
            ('exposicao', 'Exposição'),
            ('laboratorio', 'Laboratório'),
            ('transito', 'Em trânsito'),
            ('outro', 'Outro'),
        ],
        default='outro'
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
