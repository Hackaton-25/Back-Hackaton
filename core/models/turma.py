from django.db import models
from django.utils import timezone
from core.models.user import User


class Course(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)

    professor_responsavel = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="turmas_que_coordena"
    )

    ano = models.IntegerField(default=timezone.now().year)
    semestre = models.IntegerField(choices=[(1, "1º semestre"), (2, "2º semestre")], default=1)

    # Lista de alunos inscritos (muitos-para-muitos)
    alunos = models.ManyToManyField(
        User,
        blank=True,
        related_name="turmas_inscrito",
        limit_choices_to={"perfil": "aluno"},
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Turma / Course"
        verbose_name_plural = "Turmas / Courses"

    def __str__(self):
        return f"{self.nome} ({self.ano}.{self.semestre})"
