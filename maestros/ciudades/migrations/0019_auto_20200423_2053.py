# Generated by Django 3.0.4 on 2020-04-23 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciudades', '0018_auto_20200408_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='ind_capital',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Si'), (0, 'No')], default=0),
        ),
    ]