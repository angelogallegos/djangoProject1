# Generated by Django 3.2.9 on 2021-12-01 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flora', '0008_alter_estado_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='origen',
            name='Pais',
        ),
        migrations.AddField(
            model_name='especie',
            name='Pais',
            field=models.CharField(blank=True, default='', max_length=35, null=True),
        ),
    ]
