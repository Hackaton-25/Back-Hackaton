from django.db import models
from django.utils import timezone
from django.conf import settings

class Submission(models.Model):
    atividade = models.ForeignKey("core.Activity", on_delete=models.CASCADE)
    aluno = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    texto_resposta = models.TextField(blank=True)
    arquivo = models.FileField(upload_to="submissoes/", blank=True, null=True)

    nota = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Nota atribuída pelo professor"
    )

    data_envio = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("atividade", "aluno")
        ordering = ["-data_envio"]
        verbose_name = "Entrega"
        verbose_name_plural = "Entregas"

    def __str__(self):
        return f"{self.aluno.name} → {self.atividade.titulo}"
