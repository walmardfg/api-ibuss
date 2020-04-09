# Generated by Django 3.0.4 on 2020-04-08 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estados', '0011_auto_20200408_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='ind_estado',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (0, 'Inactivo')], default=1),
        ),
        migrations.AlterField(
            model_name='estado',
            name='ult_ip',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
