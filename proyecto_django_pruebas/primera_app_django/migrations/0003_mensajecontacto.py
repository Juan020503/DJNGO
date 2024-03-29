# Generated by Django 5.0.3 on 2024-03-14 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primera_app_django', '0002_tienda_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensajeContacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
