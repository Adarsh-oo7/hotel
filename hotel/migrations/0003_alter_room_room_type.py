# Generated by Django 5.0.1 on 2024-08-02 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_alter_hotelgallery_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_types', to='hotel.roomtype'),
        ),
    ]
