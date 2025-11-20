from django.db import models
from django.utils import timezone
from django.conf import settings  # importante para pegar o User personalizado

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ("active", "Ativo"),
        ("completed", "Concluído"),
        ("dropped", "Desistente"),
    ]

    aluno = models.ForeignKey(
        settings.AUTH_USER_MODEL,   # <-- AGORA É USER
        on_delete=models.CASCADE,
        related_name="matriculas"
    )

    turma = models.ForeignKey("core.Course", on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active"
    )

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("aluno", "turma")
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

    def __str__(self):
        return f"{self.aluno.name} → {self.turma.nome} ({self.status})"
