# Generated by Django 3.0.4 on 2020-04-06 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paises', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='ind_estado',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Activo')], default=1),
        ),
    ]
