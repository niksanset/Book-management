# Generated by Django 4.2.7 on 2024-01-11 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0004_author_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='slug',
        ),
    ]
