from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone


class PerfilChoices(models.TextChoices):
    ALUNO = "aluno", "Aluno"
    PROFESSOR = "professor", "Professor"
    COORDENADOR = "coordenador", "Coordenador"
    ADMIN = "admin", "Administrador"


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, perfil=PerfilChoices.ALUNO, **extra):
        if not email:
            raise ValueError("Email é obrigatório.")

        email = self.normalize_email(email)
        user = self.model(email=email, perfil=perfil, **extra)

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra):
        extra.setdefault("perfil", PerfilChoices.ADMIN)
        extra.setdefault("is_staff", True)
        extra.setdefault("is_superuser", True)

        if not password:
            raise ValueError("Superuser precisa de senha.")

        return self.create_user(email, password, **extra)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

    perfil = models.CharField(
        max_length=20,
        choices=PerfilChoices.choices,
        default=PerfilChoices.ALUNO,
    )

    # 🔥 Campos educacionais que fazem sentido no hackaton
    escola = models.CharField(max_length=255, null=True, blank=True)
    turma = models.CharField(max_length=50, null=True, blank=True)  # Ex.: 3ºA, 2ºB
    matricula = models.CharField(max_length=30, null=True, blank=True)

    # Booleans usuais
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    def __str__(self):
        return f"{self.name} ({self.email})"
