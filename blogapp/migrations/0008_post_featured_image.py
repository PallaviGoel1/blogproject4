# Generated by Django 3.2.23 on 2023-12-23 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_remove_comment_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
