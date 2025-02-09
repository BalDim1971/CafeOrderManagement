# Generated by Django 5.2a1 on 2025-02-09 14:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(10)], verbose_name='Slug'),
        ),
    ]
