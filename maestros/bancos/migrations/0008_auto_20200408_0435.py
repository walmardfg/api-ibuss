# Generated by Django 3.0.4 on 2020-04-08 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bancos', '0007_auto_20200408_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banco',
            name='ind_estado',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (0, 'Inactivo')], default=1),
        ),
    ]
