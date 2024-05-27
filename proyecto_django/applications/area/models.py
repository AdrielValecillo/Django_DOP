from django.db import models

# Create your models here.

class Area(models.Model):
    codigoArea = models.CharField("Codigo Area", max_length=10, unique=True)
    nombreArea = models.CharField("Nombre Area", max_length=30, unique=True)

    def __str__(self) -> str:
        return self.codigoArea + " - " + self.nombreArea