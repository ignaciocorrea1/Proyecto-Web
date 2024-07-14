# Generated by Django 5.0.6 on 2024-07-13 21:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CoffeKong', '0004_remove_pedido_cliente_remove_tarjeta_cliente_and_more'),
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
            name='estado',
            fields=[
                ('id_estado', models.AutoField(db_column='idEstado', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id_producto', models.IntegerField(db_column='idProducto', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=300)),
                ('precio', models.IntegerField()),
                ('imagen', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tipoProducto',
            fields=[
                ('id_tipoproducto', models.CharField(db_column='idTipoProducto', max_length=2, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
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
            name='pedido',
            fields=[
                ('id_pedido', models.AutoField(db_column='idPedido', primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('total_ped', models.IntegerField()),
                ('cliente', models.ForeignKey(db_column='run', on_delete=django.db.models.deletion.CASCADE, to='CoffeKong.cliente')),
                ('estado', models.ForeignKey(db_column='idEstado', on_delete=django.db.models.deletion.CASCADE, to='CoffeKong.estado')),
            ],
        ),
        migrations.CreateModel(
            name='detallePedido',
            fields=[
                ('id_detalle', models.AutoField(db_column='idDetalle', primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('id_pedido', models.ForeignKey(db_column='idPedido', on_delete=django.db.models.deletion.CASCADE, to='CoffeKong.pedido')),
                ('id_producto', models.ForeignKey(db_column='idProducto', on_delete=django.db.models.deletion.CASCADE, to='CoffeKong.producto')),
            ],
        ),
        migrations.CreateModel(
            name='tarjeta',
            fields=[
                ('nro_tarjeta', models.CharField(db_column='nroTarjeta', max_length=30, primary_key=True, serialize=False)),
                ('cliente', models.ForeignKey(db_column='run', on_delete=django.db.models.deletion.CASCADE, to='CoffeKong.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.ForeignKey(db_column='idTipoProducto', on_delete=django.db.models.deletion.CASCADE, to='CoffeKong.tipoproducto'),
        ),
    ]
