# Generated by Django 4.0.4 on 2022-05-28 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0004_alter_chapter_active_alter_novel_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='id',
            field=models.SlugField(max_length=511, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='title',
            field=models.CharField(max_length=511),
        ),
        migrations.AlterField(
            model_name='novel',
            name='id',
            field=models.SlugField(max_length=511, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='novel',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
