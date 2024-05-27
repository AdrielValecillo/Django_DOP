from typing import Any
from django.db import models
from applications.departamento.models import Departamento



class Formacion(models.Model):
    nombreFor = models.CharField('Nombre Curso', max_length=30, unique=True)
    descripcionFor = models.CharField('Descripcion', max_length=120, blank=True, null=True)
    
    def __str__(self) -> str:
        return str(self.id) + ' - '+ self.nombreFor + ' - '+ self.descripcionFor



class Empleado(models.Model):
    TipoVin =(
        ('1', 'Tiempo Completo'),
        ('2', 'Medio Tiempo'),
        ('3', 'Otro'),
    )

    documentEmp = models.CharField('Document Empleado', max_length=15, unique=True)
    nombreEmp = models.CharField('Nombre Empleado', max_length=60)
    tipoVinculacionEmp =models.CharField('Tipo Vinculacion', max_length=1, choices=TipoVin)
    departamentoEmp =  models.ForeignKey(Departamento, on_delete=models.CASCADE)
    formacionEmp = models.ManyToManyField(Formacion)
    
    def getTipoVin(self)->str:
        rta = 'Tiempo Completo'
        if (self.tipoVinculacionEmp == '2'):
            rta = 'Medio Tiempo'
        if (self.tipoVinculacionEmp == '2'):
            rta = 'Otro'
        return rta
    
    def __str__ (self) -> str:
        return str(self.id) + ' - '+ self.documentEmp+ " - " + self.nombreEmp + ' - '+ self.getTipoVin()
