# Generated by Django 3.2.3 on 2021-07-10 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BS', '0017_rename_reperacion_reparacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reparacion',
            name='fecha_ingreso',
            field=models.DateField(null=True),
        ),
    ]