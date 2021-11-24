# Generated by Django 3.2.9 on 2021-11-23 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flora', '0003_auto_20211123_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especie',
            name='Altura',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Autor',
            field=models.CharField(blank=True, default='0', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Estado',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='flora.estado'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Flores',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Hojas',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Humedad_Suelo',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='flora.humedad_suelo'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Imagen',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='flora.imagen'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Imagen_Perfil',
            field=models.CharField(blank=True, default='0', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Imagen_QR',
            field=models.CharField(blank=True, default='0', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Latitud',
            field=models.CharField(blank=True, default='0', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Longitud',
            field=models.CharField(blank=True, default='0', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Luminosidad',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='flora.luminosidad'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Nombre',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Nombre_Cientifico',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Origen',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='flora.origen'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='QR',
            field=models.CharField(blank=True, default='0', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Semillas',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Tipo',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='flora.tipo'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Tolerancia_Frio',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='flora.tolerancia_frio'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='Zona',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='flora.zona'),
        ),
    ]
