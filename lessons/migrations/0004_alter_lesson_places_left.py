# Generated by Django 5.2.4 on 2025-07-29 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_lesson_places_left'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='places_left',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
