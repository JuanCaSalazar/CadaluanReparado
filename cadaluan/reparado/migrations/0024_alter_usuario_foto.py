# Generated by Django 5.0.1 on 2024-10-07 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reparado', '0023_alter_solicitud_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, default='usuarios1/default.png', null=True, upload_to='usuarios/'),
        ),
    ]
