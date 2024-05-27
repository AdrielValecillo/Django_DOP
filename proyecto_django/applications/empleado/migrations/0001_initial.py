# Generated by Django 5.0.4 on 2024-05-26 19:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentEmp', models.CharField(max_length=15, unique=True, verbose_name='Document Empleado')),
                ('nombreEmp', models.CharField(max_length=60, verbose_name='Nombre Empleado')),
                ('tipoVinculacionEmp', models.CharField(choices=[('1', 'Tiempo Completo'), ('2', 'Medio Tiempo'), ('3', 'Otro')], max_length=1, verbose_name='Tipo Vinculacion')),
                ('departamentoEmp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
            ],
        ),
    ]
