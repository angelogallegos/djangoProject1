# Generated by Django 3.2.9 on 2021-12-02 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20211201_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='Apellidos',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Nombres',
            new_name='nombres',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Username',
            new_name='username',
        ),
    ]
