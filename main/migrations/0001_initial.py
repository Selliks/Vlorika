# Generated by Django 5.2.2 on 2025-06-08 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=56)),
                ('description', models.TextField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='main.size')),
            ],
        ),
    ]
