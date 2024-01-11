# Generated by Django 4.2.7 on 2024-01-09 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='author',
            name='author_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='author_book',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='BookApp.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(blank=True, to='BookApp.genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_publish',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
