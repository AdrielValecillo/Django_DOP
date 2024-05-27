from django.contrib import admin
from .models import (
    Empleado, 
    Formacion
)

# Register your models here.
admin.site.register(Empleado)
admin.site.register(Formacion)
