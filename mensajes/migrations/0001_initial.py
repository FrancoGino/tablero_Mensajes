# Generated by Django 4.2 on 2024-09-08 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remitente', models.CharField(max_length=15)),
                ('destinatario', models.CharField(max_length=15)),
                ('texto', models.TextField()),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
