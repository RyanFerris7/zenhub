# Generated by Django 4.2.11 on 2024-03-07 11:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255),
        ),
    ]
