# Generated by Django 5.0.1 on 2024-10-02 18:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reparado', '0021_compra_total_alter_compra_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='usuario',
            name='fecha_registro',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(blank=True, choices=[('ADMIN', 'Administrador'), ('TEC', 'Técnico'), ('CLI', 'Cliente'), ('USU', 'Usuario')], default='CLI', max_length=5, null=True),
        ),
    ]
