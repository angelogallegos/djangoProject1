# Generated by Django 3.2.9 on 2021-12-26 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flora', '0026_alter_especie_qr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especie',
            name='Localizacion',
            field=models.CharField(default='', max_length=900),
        ),
    ]