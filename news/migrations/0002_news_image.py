# Generated by Django 4.2.2 on 2023-08-23 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to='news/images'),
        ),
    ]
