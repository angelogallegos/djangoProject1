# Generated by Django 3.2.9 on 2021-12-14 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flora', '0014_alter_especie_imagen_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='especie',
            name='Imagen',
        ),
        migrations.AddField(
            model_name='especie',
            name='Imagen1',
            field=models.ImageField(default='', null=True, upload_to='Imagenes'),
        ),
        migrations.AddField(
            model_name='especie',
            name='Imagen2',
            field=models.ImageField(default='', null=True, upload_to='Imagenes'),
        ),
        migrations.AddField(
            model_name='especie',
            name='Imagen3',
            field=models.ImageField(default='', null=True, upload_to='Imagenes'),
        ),
        migrations.DeleteModel(
            name='Imagen',
        ),
    ]
