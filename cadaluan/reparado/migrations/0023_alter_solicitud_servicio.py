# Generated by Django 5.0.1 on 2024-10-06 22:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reparado', '0022_servicio_fecha_usuario_fecha_registro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='reparado.servicio'),
        ),
    ]
