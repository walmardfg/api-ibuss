# Generated by Django 3.0.4 on 2020-04-06 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_pais', models.CharField(max_length=200)),
                ('ind_estado', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (0, 'Inactivo')], default=1)),
                ('ult_usuario', models.CharField(max_length=100)),
                ('ult_fecha', models.DateTimeField(auto_now=True)),
                ('ult_equipo', models.CharField(max_length=200)),
                ('ult_ip', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'si_maestro_paises',
            },
        ),
    ]
