from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone


class PerfilChoices(models.TextChoices):
    USUARIO = "usuario", "Usuário"
    ADMIN = "admin", "Administrador"


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, perfil=PerfilChoices.USUARIO, **extra):
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
        default=PerfilChoices.USUARIO,
    )

    # Booleans usuais
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    def __str__(self):
        return f"{self.name} ({self.email})"
