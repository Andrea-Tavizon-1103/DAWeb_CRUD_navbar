# Generated by Django 5.1 on 2024-11-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]