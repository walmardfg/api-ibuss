# Generated by Django 3.0.4 on 2020-04-06 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paises', '0004_auto_20200406_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='ind_estado',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (0, 'Inactivo')], default=1),
        ),
    ]
