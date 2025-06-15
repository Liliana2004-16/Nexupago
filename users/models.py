from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = (
    ('Administrador', 'Administrador'),
    ('Empleado', 'Empleado'),
)

class Usuario(AbstractUser):
    identificacion = models.CharField(max_length=20, unique=True)
    cargo = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    rol = models.CharField(max_length=20, choices=ROLES)

    REQUIRED_FIELDS = ['identificacion', 'cargo', 'rol', 'email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.username} ({self.rol})"
