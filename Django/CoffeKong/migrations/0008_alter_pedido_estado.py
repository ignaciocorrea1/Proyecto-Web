# Generated by Django 5.0.6 on 2024-06-23 03:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeKong', '0007_estado_alter_pedido_cliente_pedido_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.ForeignKey(db_column='idEstado', default=0, on_delete=django.db.models.deletion.CASCADE, to='CoffeKong.estado'),
        ),
    ]
