# Generated by Django 3.2.9 on 2021-11-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Correo', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=50)),
                ('Usuario', models.CharField(max_length=20)),
                ('Contraseña', models.CharField(max_length=30)),
            ],
        ),
    ]
