# Generated by Django 3.2.9 on 2021-12-01 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flora', '0009_auto_20211201_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zona',
            name='Nombre',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
