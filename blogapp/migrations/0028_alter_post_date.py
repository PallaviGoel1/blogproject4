# Generated by Django 3.2.24 on 2024-06-23 12:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0027_auto_20240306_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
