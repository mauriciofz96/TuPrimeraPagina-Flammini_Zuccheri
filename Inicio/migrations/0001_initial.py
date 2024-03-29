# Generated by Django 5.0.1 on 2024-02-10 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_disco', models.CharField(max_length=30)),
                ('banda', models.CharField(max_length=30)),
                ('lanzamiento', models.IntegerField()),
                ('genero', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('integrantes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Musico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('instrumento', models.CharField(max_length=30)),
                ('banda', models.CharField(max_length=30)),
            ],
        ),
    ]
