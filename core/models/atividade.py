from django.db import models
from django.utils import timezone

class Activity(models.Model):
    turma = models.ForeignKey("core.Course", on_delete=models.CASCADE)
    
    titulo = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_entrega = models.DateTimeField()

    class Meta:
        ordering = ["-data_criacao"]
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"

    def __str__(self):
        return f"{self.titulo} ({self.turma.nome})"
