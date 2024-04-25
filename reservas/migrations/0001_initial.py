# Generated by Django 5.0.4 on 2024-04-11 16:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atraccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('horario_apertura', models.TimeField()),
                ('horario_cierre', models.TimeField()),
                ('capacidad_maxima', models.PositiveIntegerField()),
                ('ubicacion', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='atracciones/')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('capacidad_maxima', models.PositiveIntegerField()),
                ('lugar', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='eventos/')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_personas', models.PositiveIntegerField()),
                ('fecha_reserva', models.DateTimeField(auto_now_add=True)),
                ('atraccion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservas.atraccion')),
                ('evento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservas.evento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
