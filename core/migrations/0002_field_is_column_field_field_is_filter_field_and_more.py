# Generated by Django 5.0.1 on 2024-01-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='is_column_field',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='field',
            name='is_filter_field',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='field',
            name='is_search_field',
            field=models.BooleanField(default=False),
        ),
    ]
