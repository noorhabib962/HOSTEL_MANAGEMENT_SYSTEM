# Generated by Django 5.1.4 on 2025-01-17 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0006_alter_student_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='check_in',
            field=models.DateField(auto_now=True),
        ),
    ]
