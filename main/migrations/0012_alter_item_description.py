# Generated by Django 5.2.2 on 2025-06-19 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, max_length=512),
        ),
    ]
