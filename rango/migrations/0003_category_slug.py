# Generated by Django 5.0.3 on 2024-03-31 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_category_likes_category_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]