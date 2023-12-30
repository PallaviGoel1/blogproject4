# Generated by Django 3.2.23 on 2023-12-29 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0017_alter_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=255),
        ),
    ]
