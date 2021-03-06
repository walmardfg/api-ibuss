# Generated by Django 3.0.4 on 2020-04-08 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0007_auto_20200408_0319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='doc_indentidad',
            new_name='doc_identidad',
        ),
        migrations.AlterField(
            model_name='persona',
            name='ind_estado',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (0, 'Inactivo')], default=1),
        ),
    ]
