# Generated by Django 3.0.4 on 2020-04-23 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miscelaneos', '0012_auto_20200423_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miscelaneo',
            name='ind_estado',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (0, 'Inactivo')], default=1),
        ),
    ]
