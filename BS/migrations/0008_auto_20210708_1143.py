# Generated by Django 3.2.3 on 2021-07-08 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BS', '0007_auto_20210616_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arriendo',
            fields=[
                ('id_auto_inc', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('fecha', models.DateField()),
                ('Cancelado', models.BooleanField(default=False)),
                ('Entregado', models.BooleanField(default=False)),
                ('Finalizado', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BS.categoria')),
            ],
        ),
        migrations.RemoveField(
            model_name='sucursal',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Peluquero',
        ),
        migrations.DeleteModel(
            name='Sucursal',
        ),
    ]
