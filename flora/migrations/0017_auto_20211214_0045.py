# Generated by Django 3.2.9 on 2021-12-14 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flora', '0016_auto_20211214_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especie',
            name='Imagen1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Imagenes'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Imagen2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Imagenes'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Imagen3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Imagenes'),
        ),
    ]
