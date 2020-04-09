# Generated by Django 3.0.4 on 2020-04-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('municipios', '0006_auto_20200407_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipio',
            name='ind_estado',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Activo')], default=1),
        ),
    ]
