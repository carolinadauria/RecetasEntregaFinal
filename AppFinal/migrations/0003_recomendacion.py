# Generated by Django 4.0.4 on 2022-06-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0002_recetas_delete_recetasdulces'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recomendacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('comentarios', models.CharField(max_length=500)),
            ],
        ),
    ]
