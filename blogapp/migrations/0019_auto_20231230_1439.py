# Generated by Django 3.2.23 on 2023-12-30 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0018_auto_20231229_2334'),
    ]

    operations = [
        migrations.DeleteModel(
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]