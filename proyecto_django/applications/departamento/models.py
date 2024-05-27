from django.db import models

from applications.area.models import Area

# Create your models here.
class Departamento(models.Model):
    codigoDep = models.CharField("Codigo Departamento", max_length=10, unique=True)
    nombreDep = models.CharField("Nombre Departamento", max_length=30, unique=True)
    estadoDep = models.BooleanField("Estado", default=True)
    areaDep = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self) -> str:
        msj = "Activo"
        if(self.estadoDep == False):
            msj = "inactivo"
        
        return str(self.id)+ " - "+ self.codigoDep + " - " + self.nombreDep + " - " + msj

