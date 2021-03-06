# Generated by Django 3.0.4 on 2020-04-07 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='ind_estado',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (0, 'Inactivo')], default=1),
        ),
        migrations.AlterField(
            model_name='persona',
            name='segundo_apellido',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='segundo_nombre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefax1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono2',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
