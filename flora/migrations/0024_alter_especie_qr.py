# Generated by Django 3.2.9 on 2021-12-26 21:55

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flora', '0023_alter_especie_qr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especie',
            name='QR',
            field=models.CharField(blank=True, default=builtins.id, max_length=200, null=True, unique=True),
        ),
    ]
