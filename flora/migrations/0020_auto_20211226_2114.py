# Generated by Django 3.2.9 on 2021-12-26 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flora', '0019_auto_20211226_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='especie',
            name='Imagen_QR',
        ),
        migrations.AddField(
            model_name='especie',
            name='qr_code',
            field=models.ImageField(blank=True, default='', null=True, upload_to='qr_codes'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='QR',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
