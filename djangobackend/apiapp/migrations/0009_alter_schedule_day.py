# Generated by Django 4.0.4 on 2022-06-02 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0008_novel_first_upload_novel_rating_alter_novel_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.CharField(max_length=9),
        ),
    ]