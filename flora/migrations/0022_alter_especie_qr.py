# Generated by Django 3.2.9 on 2021-12-26 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flora', '0021_alter_especie_qr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especie',
            name='QR',
            field=models.CharField(blank=True, default=0.3503323838171236, max_length=200, null=True),
        ),
    ]
