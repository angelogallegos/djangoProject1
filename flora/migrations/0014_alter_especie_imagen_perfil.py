# Generated by Django 3.2.9 on 2021-12-01 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flora', '0013_alter_especie_imagen_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especie',
            name='Imagen_Perfil',
            field=models.ImageField(default='', null=True, upload_to='Imagen_Perfil'),
        ),
    ]
