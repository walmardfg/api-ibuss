# Generated by Django 3.0.4 on 2020-04-24 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companias', '0003_auto_20200423_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compania',
            name='ind_estado',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Activo')], default=1),
        ),
    ]
