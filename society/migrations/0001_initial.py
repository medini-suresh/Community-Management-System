# Generated by Django 4.0.1 on 2022-01-22 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import society.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to=society.models.society_image_upload_path)),
                ('owner_company', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('secretary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Societies',
            },
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bhk', models.PositiveIntegerField()),
                ('number', models.PositiveIntegerField()),
                ('floor_no', models.PositiveIntegerField()),
                ('block', models.CharField(max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='society.society')),
            ],
        ),
    ]
