# Generated by Django 3.0.4 on 2020-04-07 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ciudades', '0008_auto_20200407_2212'),
        ('miscelaneosdet', '0002_auto_20200407_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_indentidad', models.CharField(max_length=12, unique=True)),
                ('doc_fiscal', models.CharField(max_length=20)),
                ('clase_persona', models.CharField(max_length=1)),
                ('primer_apellido', models.CharField(max_length=100)),
                ('segundo_apellido', models.CharField(max_length=100)),
                ('primer_nombre', models.CharField(max_length=100)),
                ('segundo_nombre', models.CharField(max_length=100)),
                ('nombre_completo', models.CharField(max_length=100)),
                ('nombre_busqueda', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateTimeField(auto_now_add=True)),
                ('fecha_edocivil', models.DateTimeField(auto_now_add=True)),
                ('telefono1', models.CharField(max_length=20)),
                ('telefono2', models.CharField(max_length=20)),
                ('telefax1', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('es_cliente', models.BooleanField(default=False)),
                ('es_proveedor', models.BooleanField(default=False)),
                ('es_empleado', models.BooleanField(default=False)),
                ('es_otros', models.BooleanField(default=False)),
                ('ind_estado', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Activo')], default=1)),
                ('ult_usuario', models.CharField(max_length=100)),
                ('ult_fecha', models.DateTimeField(auto_now=True)),
                ('ult_equipo', models.CharField(max_length=200)),
                ('ult_ip', models.CharField(max_length=200)),
                ('id_ciudad_nacimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ciudades.Ciudad')),
                ('id_miscdet_edocivil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personas_persona_id_miscdet_edocivil', to='miscelaneosdet.DetMiscelaneo')),
                ('id_miscdet_nacionalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personas_persona_id_miscdet_nacionalidad', to='miscelaneosdet.DetMiscelaneo')),
                ('id_miscdet_sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personas_persona_id_miscdet_sexo', to='miscelaneosdet.DetMiscelaneo')),
            ],
            options={
                'db_table': 'si_maestro_personas',
            },
        ),
    ]
