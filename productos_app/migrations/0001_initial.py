# Generated by Django 5.1 on 2024-11-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('marca', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('categoria', models.CharField(max_length=20)),
                ('diseño', models.CharField(max_length=60)),
                ('calidad', models.CharField(max_length=60)),
            ],
        ),
    ]
