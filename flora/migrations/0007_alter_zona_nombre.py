# Generated by Django 3.2.9 on 2021-11-28 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flora', '0006_auto_20211123_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zona',
            name='Nombre',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
