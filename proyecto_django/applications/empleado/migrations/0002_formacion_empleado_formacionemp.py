# Generated by Django 5.0.4 on 2024-05-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreFor', models.CharField(max_length=30, unique=True, verbose_name='Nombre Curso')),
                ('descripcionFor', models.CharField(blank=True, max_length=120, null=True, verbose_name='Descripcion')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='formacionEmp',
            field=models.ManyToManyField(to='empleado.formacion'),
        ),
    ]
