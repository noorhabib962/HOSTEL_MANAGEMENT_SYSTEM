# Generated by Django 5.1.4 on 2025-01-05 08:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_management', '0002_rename_capcity_room_capacity'),
        ('student_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='hostel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hostel'),
        ),
        migrations.AddField(
            model_name='student',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hostel_management.room'),
        ),
    ]
