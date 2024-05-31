from django.urls import path
from . import views

app_name = "empleado_app"

urlpatterns = [
    path('listatodosempleados/', views.ListAllEmpleados.as_view()),
    path('listaempleadodepartamento/<valDpto>/', views.listByDptoEmpleado.as_view()),
    path('listadobusquedaempleado/', views.listEmpleadoByKword.as_view()),
    path('listadoempleadospaginados/', views.listAllEmpleadosPag.as_view()),
    path('crearEmpleado/', views.CreateEmpleado.as_view()),
    path('successempleado/', views.SuccessEmpleado.as_view(), name='proceso_correcto'),
    path('verempleado/<pk>', views.DetailEmpleado.as_view()),
]
