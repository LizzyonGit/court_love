# Generated by Django 5.2.4 on 2025-07-25 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_alter_capacity_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='places_left',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
