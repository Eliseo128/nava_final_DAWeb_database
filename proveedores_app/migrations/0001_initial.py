# Generated by Django 5.1.1 on 2024-11-19 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id_proveedor', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('tipo_producto', models.CharField(max_length=20)),
                ('horario', models.TimeField()),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=40)),
            ],
        ),
    ]
