# Generated by Django 4.0.4 on 2022-05-27 20:42

import apiapp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id', models.SlugField(max_length=250, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('alternativetitle', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('genres', models.TextField()),
                ('tags', models.TextField()),
                ('status', models.IntegerField()),
                ('release', models.IntegerField()),
                ('completed', models.IntegerField()),
                ('last_updated', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=apiapp.models.upload_to, verbose_name='Image')),
                ('active', models.BooleanField()),
                ('views', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('novel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apiapp.novel')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.SlugField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(null=True)),
                ('date', models.DateField(null=True)),
                ('chapterNumber', models.IntegerField(null=True)),
                ('section', models.IntegerField()),
                ('active', models.BooleanField()),
                ('novel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiapp.novel')),
            ],
        ),
    ]
