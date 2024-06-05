# Generated by Django 5.0.6 on 2024-06-05 02:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeKong', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('run', models.CharField(db_column='run', max_length=12, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=80)),
                ('apaterno', models.CharField(max_length=30)),
                ('amaterno', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=50)),
                ('contrasenia', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('id_pedido', models.IntegerField(db_column='idPedido', primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='vendedor',
            fields=[
                ('run', models.CharField(db_column='run', max_length=12, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=80)),
                ('apaterno', models.CharField(max_length=30)),
                ('amaterno', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=50)),
                ('contrasenia', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='detallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('id_producto', models.ForeignKey(db_column='idProducto', on_delete=django.db.models.deletion.CASCADE, to='CoffeKong.producto')),
                ('id_pedido', models.ForeignKey(db_column='idPedido', on_delete=django.db.models.deletion.CASCADE, to='CoffeKong.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='tarjeta',
            fields=[
                ('nro_tarjeta', models.CharField(db_column='nroTarjeta', max_length=30, primary_key=True, serialize=False)),
                ('run', models.ForeignKey(db_column='run', on_delete=django.db.models.deletion.CASCADE, to='CoffeKong.cliente')),
            ],
        ),
    ]
