from django.db import models
from django.utils import timezone
from django.conf import settings

class Feedback(models.Model):
    aluno = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="feedbacks_recebidos")
    professor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="feedbacks_enviados")
    turma = models.ForeignKey("core.Course", on_delete=models.CASCADE)


    texto = models.TextField()

    nota_opcional = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Usado apenas quando o feedback tiver avaliação numérica"
    )

    criado_em = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-criado_em"]
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"

    def __str__(self):
        return f"Feedback de {self.professor} → {self.aluno} ({self.turma})"
