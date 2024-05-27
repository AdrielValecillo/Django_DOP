from django.urls import path
from . import views

urlpatterns = [
    path('listatodosempleados/', views.ListAllEmpleados.as_view()),
    path('listaempleadodepartamento/<valDpto>/', views.listByDptoEmpleado.as_view()),
    path('listadobusquedaempleado/', views.listEmpleadoByKword.as_view()),
    path('listadoempleadospaginados/', views.listAllEmpleadosPag.as_view()),
]
