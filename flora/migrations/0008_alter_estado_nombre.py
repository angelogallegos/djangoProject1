# Generated by Django 3.2.9 on 2021-12-01 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flora', '0007_alter_zona_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='Nombre',
            field=models.CharField(max_length=40),
        ),
    ]
