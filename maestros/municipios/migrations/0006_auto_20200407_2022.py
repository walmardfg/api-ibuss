# Generated by Django 3.0.4 on 2020-04-07 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('municipios', '0005_auto_20200407_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipio',
            name='ind_estado',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (0, 'Inactivo')], default=1),
        ),
    ]
