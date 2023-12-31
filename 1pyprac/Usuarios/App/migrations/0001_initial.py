# Generated by Django 4.0.6 on 2023-07-19 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('CursoId', models.AutoField(primary_key=True, serialize=False)),
                ('Imagen', models.ImageField(null=True, upload_to='images/curso')),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=50)),
                ('Horas', models.IntegerField(default=0)),
                ('Costo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('CategoriaID', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=50)),
                ('Estado', models.BooleanField()),
                ('CursoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.cursos')),
            ],
        ),
    ]
