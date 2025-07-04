# Generated by Django 5.2.3 on 2025-06-24 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenamiento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barriociudadela',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='barriociudadela',
            name='numero_edificios_residenciales',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='barriociudadela',
            name='numero_parques',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='barriociudadela',
            name='numero_viviendas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='parroquia',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='parroquia',
            name='tipo',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='parroquia',
            name='ubicacion',
            field=models.CharField(max_length=10),
        ),
    ]
