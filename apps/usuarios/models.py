from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    # Los campos borrados ya los incluye el modelo AbstractUser aunque se pueden sobreescribir

    dni = models.IntegerField(default=None,null=True)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.CharField(max_length=50)
    fecha_registro = models.DateField(blank=True, null=True)
    nro_telefonico = models.CharField(max_length=15, blank=True, null=True)

    # Se pueden usar estos atributos si quieren personalizar mas
    # EMAIL_FIELD = "email"
    # USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ["email"]