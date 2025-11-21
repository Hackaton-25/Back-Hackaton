from django.db import models

class Coletor(models.Model):
    nome = models.CharField(max_length=255)
    biografia = models.TextField(blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
