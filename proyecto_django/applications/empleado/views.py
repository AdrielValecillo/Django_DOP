from django.shortcuts import render
from django.views.generic import ListView
from typing import Any
from django.db.models.query import QuerySet

from .models import Empleado
# Create your views here.

class ListAllEmpleados(ListView):
    template_name = 'empleado/list_all.html'
    model = Empleado


class listByDptoEmpleado(ListView):
    template_name = 'empleado/list_by_dpto.html'
    

    def get_queryset(self):
        x = self.kwargs['valDpto']
        rtaLista = Empleado.objects.filter(
            departamentoEmp__nombreDep = x
        )
        return rtaLista
    
class listEmpleadoByKword(ListView):
    template_name = 'empleado/find_empleado.html'
    context_object_name = 'rtaEmpleados'
    
    def get_queryset(self):
        x = self.request.GET.get("valNom", '')
        rtaLista = Empleado.objects.filter(
            nombreEmp = x
        )
        return rtaLista()
    
class listAllEmpleadosPag(ListView):
    template_name = 'empleado/list_all_pag.html'
    model = Empleado
    paginate_by = 3
    ordering = 'nombreEmp'
